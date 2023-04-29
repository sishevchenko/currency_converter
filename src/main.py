import asyncio
import logging
from datetime import datetime

from fastapi import FastAPI

from src.currencies.router import router as currencies_router
from src.currencies.utils import start_create_or_update_currencies_info

app = FastAPI(
    title="Currency Converter"
)

app.include_router(currencies_router)


async def start():
    while True:
        await start_create_or_update_currencies_info()
        await asyncio.sleep(43200)  # 12 hours


logging.basicConfig(level=logging.INFO, filename="info_log.log", filemode="a")
logging.info(f"Project started at {datetime.utcnow()}\n{'-' * 100}")

loop = asyncio.get_running_loop()
loop.create_task(start())
