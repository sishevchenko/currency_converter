import aiohttp
import logging
from datetime import datetime

from sqlalchemy.dialects.postgresql import insert

from src.config import API_KEY
from src.currencies.models import Currency
from src.db import engine


async def create_or_update_currency_info(api_key: str, code_name: list) -> dict:
    async with engine.begin() as session:
        code, name = code_name
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{code}"
        async with aiohttp.ClientSession() as connection:
            async with connection.get(url=url) as response:
                response = await response.json()
                if response["result"] == "success":
                    conversion_rates = response["conversion_rates"]
                    stmt = insert(Currency).values(name=name, code=code, rates=conversion_rates)
                    on_conflict_do_update_stmt = stmt.on_conflict_do_update(
                        index_elements=["code", "id"],
                        set_=dict(name=name, rates=conversion_rates))
                    await session.execute(on_conflict_do_update_stmt)
                    await session.commit()
                    return conversion_rates


async def start_create_or_update_currencies_info(api_key=API_KEY):
    logging.basicConfig(level=logging.INFO, filename="info_log.log", filemode="a")
    logging.info(f"DataBase update started at {datetime.utcnow()}")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    async with aiohttp.ClientSession() as connection:
        async with connection.get(url=url) as response:
            response = await response.json()
            if response["result"] == "success":
                supported_codes = response["supported_codes"]
                for code_name in supported_codes:
                    await create_or_update_currency_info(api_key=api_key, code_name=code_name)
