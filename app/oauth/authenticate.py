from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from sqlmodel import select, Session
from app import config
from .models import User, TokenData
from ..core.database import SessionDep, get_session


password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, hashed_password: str) -> str:
    """Verify if password and hash matched
    """
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a string password
    """
    return password_hash.hash(password)


def get_user(session: SessionDep, username: str) -> User | None:
    """Get user by username in database
    """
    query = select(User).where(User.username == username)
    user: User | None = session.exec(query).first()
    return user


def authenticate_user(session: SessionDep, username: str, password: str) -> bool | User:
    """Verify if the user password matched within the database
    """
    try:
        user: User | None = get_user(session, username)
        if not verify_password(password, user.password):
            return False
        return user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Encode jwt token with given expiration time
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(
    db: Session = Depends(get_session), 
    token: str = Depends(oauth2_scheme)
) -> User:
    """Decode and check access token to get the current user

    returns: user = current user based from decoded token
    exception: raise 401 if token is invalid
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user
