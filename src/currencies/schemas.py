from typing import Dict
from pydantic import BaseModel


class CurrencyRead(BaseModel):
    name: str
    code: str
    rates: Dict
