from typing import List, Dict
from fastapi import APIRouter, Depends
from sqlmodel import select
from .models import Address
from ..core.database import SessionDep
from ..oauth.authenticate import get_current_user
from ..oauth.models import User
from ..core.loggger import RouteLogger


router = APIRouter(
    prefix="/address",
    route_class=RouteLogger,
    dependencies=[Depends(get_current_user)]
)


@router.get("/")
async def list_address(session: SessionDep, user: User = Depends(get_current_user)) -> List[Address]:
    return session.exec(
        select(Address).where(Address.user == user)
    ).all()


@router.get("/{add_id}")
async def get_address(add_id: str, session: SessionDep, user: User = Depends(get_current_user)) -> Address:
    return session.exec(
        select(Address).where(Address.user == user, Address.id == add_id)
    ).first()


@router.post("/")
async def create_address(add: Address, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Address:
    Address.model_validate(add)
    add.user = user
    session.add(add)
    session.commit()
    session.refresh(add)
    return add


@router.patch("/{add_id}")
async def update_address(add_id: int, add: Address, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Address:
    Address.model_validate(add)
    db_data = session.exec(
        select(Address).where(Address.user == user, Address.id == add_id)
    ).first()
    data = add.model_dump(exclude_unset=True)
    db_data.sqlmodel_update(data)

    session.add(db_data)
    session.commit()
    session.refresh(db_data)
    return db_data


@router.delete("/{add_id}")
async def delete_address(add_id: int, session: SessionDep,
                         user: User = Depends(get_current_user)) -> Dict:
    db_data = session.exec(
        select(Address).where(Address.user == user, Address.id == add_id)
    ).first()
    session.delete(db_data)
    session.commit()
    return {"ok": True}
