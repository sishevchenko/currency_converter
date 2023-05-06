import asyncio
import logging
from datetime import datetime

from fastapi import FastAPI

from src.currencies.router import router as currencies_router
from src.currencies.utils import start_auto_update_db
from src.config import DEBUG


app = FastAPI(
    title="Currency Converter"
)

app.include_router(currencies_router)

if not DEBUG:
    logging.basicConfig(level=logging.INFO, filename="info_log.log", filemode="a")
    logging.info(f"Project started at {datetime.utcnow()}\n{'-' * 100}")

    loop = asyncio.get_running_loop()
    loop.create_task(start_auto_update_db())
