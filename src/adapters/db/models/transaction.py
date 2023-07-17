from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .account import Account
from .base import BaseModel


class Transaction(BaseModel):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    operation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(),
        server_default=func.now(),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(String(255))
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    account: Mapped["Account"] = relationship(back_populates="transactions")

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, operation_date={self.operation_date!r})"
