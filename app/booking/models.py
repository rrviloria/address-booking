from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

from ..oauth.models import User


class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    longitude: float
    latitude: float
    name: str = Field(default="")
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="address")


class Location(BaseModel):
    longitude: float
    latitude: float
    distance: int
