from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from src.db import BaseMeta
from src.models import BaseModel


class Currency(BaseModel, BaseMeta):
    __tablename__ = "currency"

    name: Mapped[str] = mapped_column(String, nullable=True)
    code: Mapped[str] = mapped_column(String, primary_key=True)
    rates: Mapped[JSON] = mapped_column(JSON)

    def __str__(self):
        return "{} {} {}".format(self.name, self.code, self.rates)
