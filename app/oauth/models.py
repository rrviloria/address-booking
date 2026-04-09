from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

from typing import TYPE_CHECKING

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
