from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship
from ..oauth.models import User


class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    longitude: Decimal = Field(max_digits=9, decimal_places=6)
    latitude: Decimal = Field(max_digits=9, decimal_places=6)
    name: str = Field(default="")
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="address")
