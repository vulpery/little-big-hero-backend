import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.services.user import UserService
from app.core.database import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    try:
        db_user = UserService.create_user(db, user_create)
        return db_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{wallet_address}", response_model=UserRead)
def read_user(wallet_address: str, db: Session = Depends(get_db)):
    """
    Retrieve a user by wallet address.
    """
    db_user = UserService.get_user(db, wallet_address)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    """
    Retrieve all users.
    """
    return UserService.get_users(db)


@router.put("/{wallet_address}", response_model=UserRead)
def update_user(
    wallet_address: str, user_update: UserUpdate, db: Session = Depends(get_db)
):
    """
    Update an existing user's information.
    """
    db_user = UserService.update_user(db, wallet_address, user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{wallet_address}", response_model=dict)
def delete_user(wallet_address: str, db: Session = Depends(get_db)):
    """
    Delete a user by wallet address.
    """
    result = UserService.delete_user(db, wallet_address)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
