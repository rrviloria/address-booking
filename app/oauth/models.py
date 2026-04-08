from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    address: list["Address"] = Relationship(back_populates="user")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
