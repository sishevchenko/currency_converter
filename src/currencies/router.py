from decimal import Decimal

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.currencies.models import Currency
from src.db import get_async_session

router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)


@router.get("/all")
async def get_all_currencies_rates(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Currency.code, Currency.rates)
        currencies = await session.execute(query)
        return currencies.__dict__["iterator"]
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/supported")
async def get_all_supported_currency(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Currency.code, Currency.name)
        supported = await session.execute(query)
        supported = dict(supported.__dict__["iterator"])
        return {"total": len(supported), "supported": supported}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/{target_code}")
async def get_currency_rates(target_code: str, session: AsyncSession = Depends(get_async_session)):
    try:
        target_code = target_code.upper()
        query = select(Currency).where(Currency.code == target_code)
        currency = await session.execute(query)
        try:
            return currency.scalars().one()
        except NoResultFound as ex:
            return {target_code: "Not found"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/convert/{base_code}/{target_code}/{quantity}")
async def get_conversion(base_code: str, target_code: str, quantity: Decimal,
                         session: AsyncSession = Depends(get_async_session)):
    try:
        base_code = base_code.upper()
        target_code = target_code.upper()
        query = select(Currency).where(Currency.code == base_code)
        currency = await session.execute(query)
        try:
            currency = currency.scalars().one()
            rates = Decimal(currency.rates[target_code])
            return {f"{quantity} {base_code} to {target_code}": quantity * rates}
        except KeyError as ex:
            return {target_code: "Unsupported"}
        except NoResultFound as ex:
            return {base_code: "Not found"}
    except Exception as ex:
        raise HTTPException(status_code=200, detail={
            "status": "error",
            "data": None,
            "details": ex
        })
