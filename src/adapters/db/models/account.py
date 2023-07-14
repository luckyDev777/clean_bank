from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import BaseModel
from .transaction import Transaction


class Account(BaseModel):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_number: Mapped[str] = mapped_column(String(20))
    balance: Mapped[float] = mapped_column(nullable=False)
    customer_id = ForeignKey("customers.id")
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="account")

    def __repr__(self) -> str:
        return f"Account(id={self.id!r}, customer_id={self.customer_id!r}, balance={self.balance!r})"
