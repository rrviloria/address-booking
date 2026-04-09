from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from geopy import distance

from ..core.database import SessionDep
from ..core.loggger import RouteLogger
from ..oauth.authenticate import get_current_user
from ..oauth.models import User
from .models import Address, Location
from .service import AddressService

router = APIRouter(
    prefix="/address", route_class=RouteLogger, dependencies=[Depends(get_current_user)]
)


@router.get("/")
async def list_address(
    session: SessionDep, user: User = Depends(get_current_user)
) -> List[Address]:
    return AddressService().get(session, {"user": user})


@router.get("/{add_id}")
async def get_address(
    add_id: str, session: SessionDep, user: User = Depends(get_current_user)
) -> Address:
    results = AddressService().get(session, {"user": user})
    if len(results) > 0:
        return results[0]
    else:
        raise HTTPException(status_code=404, detail="Address not found")


@router.post("/")
async def create_address(
    add: Address, session: SessionDep, user: User = Depends(get_current_user)
) -> Address:
    """API route for creating address in database"""
    add.user = user
    return AddressService().create(session, add)


@router.patch("/{add_id}")
async def update_address(
    add_id: int,
    add: Address,
    session: SessionDep,
    user: User = Depends(get_current_user),
) -> Address:
    filters = {"user": user, "id": add_id}
    return AddressService().update(session, filters, add)


@router.delete("/{add_id}")
async def delete_address(
    add_id: int, session: SessionDep, user: User = Depends(get_current_user)
) -> Dict:
    filters = {"user": user, "id": add_id}
    AddressService().delete(session, filters)
    return {"ok": True}


@router.post("/nearme")
async def near_me(
    location: Location, session: SessionDep, user: User = Depends(get_current_user)
) -> dict:
    addresses = AddressService().get(session, {"user": user})
    locations = {item.name: (item.longitude, item.latitude) for item in addresses}
    my_loc = (location.longitude, location.latitude)

    closest_site = min(
        locations.keys(), key=lambda k: distance.distance(my_loc, locations[k]).km
    )
    km_dist = distance.distance(my_loc, locations[closest_site]).km

    return {closest_site: f"{km_dist} km"}
