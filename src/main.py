import asyncio
from fastapi import FastAPI

from src.currencies.router import router as currencies_router
from src.currencies.utils import start_create_or_update_currencies_info

app = FastAPI(
    title="Currency Converter"
)

app.include_router(currencies_router)


@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_running_loop()
    print("Start coroutine start_create_or_update_currencies_info")
    await loop.create_task(start_create_or_update_currencies_info())
    print("End coroutine start_create_or_update_currencies_info")
    # await asyncio.sleep(43200)  # 12 hours
