from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from src.config import BOT_TOKEN

from src.bot.handler import get_start_handler
from src.bot.handler import get_help_handler
from src.bot.handler import get_all_supported_currency_handler
from src.bot.handler import get_currency_rates_handler
from src.bot.handler import get_conversion_handler
from src.bot.handler import send_echo_handler

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

dp.message.register(get_start_handler, Command(commands=["start"]))
dp.message.register(get_help_handler, Command(commands=['help']))
dp.message.register(get_all_supported_currency_handler, Command(commands=['supported']))
dp.message.register(get_currency_rates_handler, Command(commands=['rates']))
dp.message.register(get_conversion_handler, Command(commands=['convert']))
dp.message.register(send_echo_handler)


async def start_bot():
    await dp.start_polling(bot)
