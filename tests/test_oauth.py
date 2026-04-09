from app.oauth.models import User
from app.oauth.authenticate import get_password_hash


def test_authenticate(client, db_session):
    """Test for simple jwt/bearer authentication route
    were access token should be created
    """
    user = User(username="rayray", password=get_password_hash("Isturtleblue?"))
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    resp = client.post(
        "/token", data={"username": "rayray", "password": "Isturtleblue?"}
    )
    assert resp.status_code == 200
    # assert that access token was created
    assert "access_token" in resp.json()


def test_create_user(client):
    """Test creation of authencation user used for
    accessing address routes
    """
    resp = client.post(
        "/users", json={"username": "rayray", "password": "Isturtleblue?"}
    )
    assert resp.status_code == 200
    # make sure password was saved in hash
    assert resp.json()["password"] != "Isturtleblue?"
