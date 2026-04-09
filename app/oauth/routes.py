from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from .authenticate import authenticate_user, create_access_token, get_password_hash
from .models import User, Token
from ..core.database import SessionDep
from app import config
from .service import UserService


router = APIRouter()


@router.post("/token")
async def login(session: SessionDep,
                account: OAuth2PasswordRequestForm = Depends()) -> Token:
    """API route for user account login that requires username/password
    to receive access token
    """
    user = authenticate_user(session, account.username, account.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/users")
async def create_user(user: User, session: SessionDep) -> User:
    """API route for creating user account
    """
    # TODO: authenticate
    user.password = get_password_hash(user.password)
    return UserService().create(session, user)
