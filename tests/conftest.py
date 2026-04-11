import random

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app import config
from app.booking.models import Address
from app.core.database import get_session
from app.main import app
from app.oauth.authenticate import User, get_current_user

TEST_DB_URL = f"sqlite:///./{config.SQLITE_TESTDB_NAME}"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = Session(engine)


async def mock_session():
    with Session(engine) as session:
        yield session


@pytest.fixture
def mock_user():
    return User(username="rayray", password="turtleisgreen")


@pytest.fixture(scope="function")
def db_session():
    """Fixture for test db"""
    SQLModel.metadata.create_all(bind=engine)
    session = TestingSessionLocal
    try:
        yield session
    finally:
        session.close()
        SQLModel.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session, mock_user):
    """Fixture for testclient"""

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    def override_get_current_user():
        return mock_user

    app.dependency_overrides[get_session] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def setup_db():
    """Autouse fixture for clearing data before running a test"""
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)


@pytest.fixture
def mock_address(db_session, mock_user):
    """Mock address creation"""
    n = 10
    address = []
    for _ in range(n):
        add = Address(
            latitude=random.randrange(155, 390),
            longitude=random.randrange(155, 390),
            user=mock_user,
        )
        db_session.add(add)
        db_session.commit()
        address.append(add)
    return address
