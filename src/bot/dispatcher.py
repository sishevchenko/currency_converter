from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from src.config import BOT_TOKEN

from src.bot.handler import get_start_bot
from src.bot.handler import get_help_bot
from src.bot.handler import get_all_supported_currency_bot
from src.bot.handler import get_currency_rates_bot
from src.bot.handler import get_conversion_bot
from src.bot.handler import send_echo_bot

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

dp.message.register(get_start_bot, Command(commands=["start"]))
dp.message.register(get_help_bot, Command(commands=['help']))
dp.message.register(get_all_supported_currency_bot, Command(commands=['supported']))
dp.message.register(get_currency_rates_bot, Command(commands=['rates']))
dp.message.register(get_conversion_bot, Command(commands=['convert']))
dp.message.register(send_echo_bot)


async def start_bot():
    await dp.start_polling(bot)
