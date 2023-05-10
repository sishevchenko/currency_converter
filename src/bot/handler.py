from decimal import Decimal

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.bot.localization import language
from src.bot.state_machine import StateConversion, StateRates
from src.currencies.models import Currency
from src.db import async_session_maker


async def get_start_handler(message: Message):
    await message.answer(language["start"]["ru" if message.from_user.language_code == "ru" else "en"])


async def get_help_handler(message: Message):
    await message.answer(language["help"]["ru" if message.from_user.language_code == "ru" else "en"])


async def set_conversion_state(message: Message, state: FSMContext):
    await state.set_state(StateConversion.SET_BASE_TARGET_QUANTITY)
    await message.answer(language["conversion_state"]["ru" if message.from_user.language_code == "ru" else "en"])


async def get_conversion_handler(message: Message, state: FSMContext):
    try:
        base_code = message.text.split()[-3].upper()
        target_code = message.text.split()[-2].upper()
        quantity = Decimal(message.text.split()[-1])
        async with async_session_maker() as session:
            query = select(Currency).where(Currency.code == base_code)
            currency = await session.execute(query)
            try:
                currency = currency.scalars().one()
                rates = Decimal(currency.rates[target_code])
                await message.answer(f"{quantity} {base_code} = {round(quantity * rates, 2)} {target_code}")
            except KeyError as ex:
                await message.answer(f"{target_code}: Unsupported\n/supported")
            except NoResultFound as ex:
                await message.answer(f"{base_code}: Not found\n/supported")
    except Exception as ex:
        await message.answer("Ой, что-то пошло не так :(\n/help")
    finally:
        await state.clear()


async def set_rates_state(message: Message, state: FSMContext):
    await state.set_state(StateRates.SET_TARGET)
    await message.answer(language["rates_state"]["ru" if message.from_user.language_code == "ru" else "en"])


async def get_currency_rates_handler(message: Message, state: FSMContext):
    try:
        target_code = message.text.split()[-1].upper()
        async with async_session_maker() as session:
            query = select(Currency).where(Currency.code == target_code)
            currency = await session.execute(query)
        try:
            currency = currency.scalars().one()
            text = "{}{}".format(f"{currency.name} \"{currency.code}\"\n",
                                 "\n".join([f"{code}: {round(rate, 2)}" for code, rate in currency.rates.items()]))
            await message.answer(text)
        except NoResultFound as ex:
            return {target_code: "Not found\n/supported"}
    except Exception as ex:
        await message.answer("Ой, что-то пошло не так :(\n/help")
    finally:
        await state.clear()


async def get_all_supported_currency_handler(message: Message):
    try:
        async with async_session_maker() as session:
            query = select(Currency.code, Currency.name)
            supported = await session.execute(query)
            supported = dict(supported.__dict__["iterator"])
            await message.answer("\n".join([f"{code} {name}" for code, name in supported.items()]))
    except Exception as ex:
        await message.answer(str(ex))


async def send_echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Ой, что-то пошло не так :(\n/help")
