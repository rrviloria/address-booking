import random

from app.booking.models import Address


def test_create_address(client):
    """Test success create address response"""
    response = client.post(
        "/address",
        json={"longitude": 123.5, "latitude": 456.6},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "latitude": 456.6,
        "longitude": 123.5,
        "name": "",
        "user_id": 1,
    }


def test_list_address(client, mock_address):
    """Test success get list address and response length
    should be the same as mocked data
    """

    response = client.get("/address")

    assert response.status_code == 200
    assert len(response.json()) == len(mock_address)


def test_get_address(client, mock_address):
    """Test success response for get single address route"""
    response = client.get(f"/address/{mock_address[5].id}")

    assert response.status_code == 200
    assert response.json()["id"] == mock_address[5].id


def test_delete_address(client, db_session, mock_user):
    """Test success delete route for address and check the response"""
    add = Address(
        latitude=random.randrange(155, 390),
        longitude=random.randrange(155, 390),
        user=mock_user,
    )
    db_session.add(add)
    db_session.commit()
    db_session.refresh(add)

    response = client.delete(f"/address/{add.id}")

    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_update_address(client, db_session, mock_user):
    """Test success patch route for address and make sure
    that the data were updated properly
    """
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
        json={"longitude": 123.5, "latitude": 456.6},
    )
    resp_data = response.json()
    assert response.status_code == 200
    # values should be updated properly
    assert resp_data["longitude"] == 123.5
    assert resp_data["latitude"] == 456.6
