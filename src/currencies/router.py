from decimal import Decimal

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.currencies.models import Currency
from src.db import get_async_session

router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)


@router.get("/")
async def get_all_currency(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Currency)
        res = await session.execute(query)
        return res.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/{curr}/{target_curr}/{quantity}")
async def get_convert(base_code: str, target_code: str, quantity: Decimal,
                      session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Currency).where(Currency.code == base_code)
        currency = await session.execute(query)
        return currency.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })
