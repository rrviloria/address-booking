import random
from app.booking.models import Address


def test_create_address_validation(client):
    response = client.post(
        "/address",
        json={"longitude": 123.5},
    )

    assert response.status_code == 422
    assert "errors" in response.json()


def test_update_address_validation(client, db_session, mock_user):
    add = Address(
        latitude=random.randrange(155, 390),
        longitude=random.randrange(155, 390),
        user=mock_user,
    )
    db_session.add(add)
    db_session.commit()
    db_session.refresh(add)

    response = client.patch(
        f"/address/{add.id}",
        json={"longitude": 123.5},
    )

    assert response.status_code == 422
    assert "errors" in response.json()


def test_get_address_not_found(client, db_session, mock_user):
    response = client.get("/address/30")

    assert response.status_code == 422
    assert "errors" in response.json()
