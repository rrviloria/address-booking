from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from .models import Address
from ..core.database import SessionDep
from ..oauth.authenticate import get_current_user
from ..oauth.models import User
from ..core.loggger import RouteLogger
from .service import AddressService


router = APIRouter(
    prefix="/address",
    route_class=RouteLogger,
    dependencies=[Depends(get_current_user)]
)


@router.get("/")
async def list_address(session: SessionDep, user: User = Depends(get_current_user)) -> List[Address]:
    return AddressService().get(session, {"user": user})


@router.get("/{add_id}")
async def get_address(add_id: str, session: SessionDep, user: User = Depends(get_current_user)) -> Address:
    results = AddressService().get(session, {"user": user})
    if len(results) > 0:
        return results[0]
    else:
        raise HTTPException(status_code=404, detail="Address not found")


@router.post("/")
async def create_address(add: Address, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Address:
    """API route for creating address in database
    """
    add.user = user
    return AddressService().create(session, add)


@router.patch("/{add_id}")
async def update_address(add_id: int, add: Address, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Address:
    filters = {
        "user": user,
        "id": add_id
    }
    return AddressService().update(session, filters, add)


@router.delete("/{add_id}")
async def delete_address(add_id: int, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Dict:
    filters = {
        "user": user,
        "id": add_id
    }
    AddressService().delete(session, filters)
    return {"ok": True}
