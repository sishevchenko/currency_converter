import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

sys.path.append(os.path.join("\\".join(sys.path[0].split("\\")[:-2])))

from src.config import BOT_TOKEN

from src.bot.handler import process_start_command
from src.bot.handler import process_help_command
from src.bot.handler import get_all_supported_currency
from src.bot.handler import get_currency_rates
from src.bot.handler import get_conversion
from src.bot.handler import send_echo


bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(get_conversion, Command(commands=['convert']))
dp.message.register(get_currency_rates, Command(commands=['rates']))
dp.message.register(get_all_supported_currency, Command(commands=['supported']))
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
