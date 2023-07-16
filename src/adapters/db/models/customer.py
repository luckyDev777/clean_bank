from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import BaseModel
from .account import Account


class Customer(BaseModel):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    accounts: Mapped[list["Account"]] = relationship(back_populates="customer", lazy="joined") 

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, name={self.name!r}, email={self.email!r})"