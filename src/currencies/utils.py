from datetime import datetime
import asyncio
import logging

import aiohttp
from sqlalchemy.dialects.postgresql import insert

from src.config import API_KEY
from src.currencies.models import Currency
from src.db import engine


async def on_conflict_do_update_currency(api_key: str, code_name: list) -> None:
    """this func receives a currency code and its decryption as input and requests the API for the current
    exchange rate of the requested currency, after which it writes the received data to the database """

    code, name = code_name
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{code}"
    async with aiohttp.ClientSession() as connection:
        async with connection.get(url=url) as response:
            response = await response.json()
            if response["result"] == "success":
                conversion_rates = response["conversion_rates"]
                async with engine.begin() as session:
                    stmt = insert(Currency).values(name=name, code=code, rates=conversion_rates)
                    on_conflict_do_update_stmt = stmt.on_conflict_do_update(
                        index_elements=["code"],
                        set_=dict(name=name, rates=conversion_rates))
                    await session.execute(on_conflict_do_update_stmt)
                    await session.commit()


async def start_create_or_update_currencies(api_key=API_KEY) -> None:
    """this func receives an api_key (.env API_KEY by default) as input to access the exchangerate API,
    receives a list of available codes from the API and calls the on_conflict_do_update_currency func,
    passing it an api_key and a code from the list of available """

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    async with aiohttp.ClientSession() as connection:
        async with connection.get(url=url) as response:
            response = await response.json()
            if response["result"] == "success":
                supported_codes = response["supported_codes"]
                for code_name in supported_codes:
                    await on_conflict_do_update_currency(api_key=api_key, code_name=code_name)


async def start_auto_update_db() -> None:
    """this func starts an infinite loop of automatic update of the database once every 12 hours by calling
    start_create_or_update_currencies and slowing down until the next call in the event_loop """

    while True:
        logging.basicConfig(level=logging.INFO, filename="info_log.log", filemode="a")
        logging.info(f"DataBase update started at {datetime.utcnow()}")
        await start_create_or_update_currencies()
        logging.info(f"DataBase update end at {datetime.utcnow()}")
        await asyncio.sleep(43200)  # 12 hours
