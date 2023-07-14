from datetime import datetime
from sqlalchemy import ForeignKey, String, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel


class Transaction(BaseModel):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Numeric] = mapped_column(nullable=False)
    operation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(),
        server_default=func.now(),
        nullable=False
    )
    description: Mapped[str] = mapped_column(String(255))
    account_id = ForeignKey("accounts.id")

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, operation_date={self.operation_date!r})"
