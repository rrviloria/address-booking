from typing import TYPE_CHECKING

from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.booking.models import Address


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str
    username: str = Field(unique=True, index=True)
    address: list["Address"] = Relationship(back_populates="user")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
