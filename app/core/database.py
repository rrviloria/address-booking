from typing import Annotated

from fastapi import Depends

from sqlmodel import Session, SQLModel, create_engine
from app import config


connect_args = {"check_same_thread": False}
engine = create_engine(config.SQLITE_URL, connect_args=connect_args)

def create_db_and_tables():
    """Create all data models in database
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """Generator for yielding database session
    """
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
