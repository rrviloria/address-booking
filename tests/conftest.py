import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.core.database import get_session
from app.main import app
from app.oauth.authenticate import User, get_current_user

test_db_url = "sqlite:///./test.db"
engine = create_engine(test_db_url, connect_args={"check_same_thread": False})
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
