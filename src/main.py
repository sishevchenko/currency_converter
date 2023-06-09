import asyncio
import logging
from datetime import datetime

from fastapi import FastAPI

from src.currencies.router import router as currencies_router
from src.currencies.utils import start_auto_update_db
from src.config import DEBUG, BOT_START

from src.bot.dispatcher import start_bot


app = FastAPI(
    title="Currency Converter",
    debug=DEBUG,
    version="1.0.0"
)

app.include_router(currencies_router)


loop = asyncio.get_running_loop()

if not DEBUG:
    logging.basicConfig(level=logging.INFO, filename="info_log.log", filemode="a")
    logging.info(f"Project started at {datetime.utcnow()}\n{'-' * 100}")

    loop.create_task(start_auto_update_db())


if BOT_START:
    loop.create_task(start_bot())
