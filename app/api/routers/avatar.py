from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.services.avatar import AvatarService
from app.core.database import get_db
from app.schemas.avatar import AvatarCreate, AvatarRead, AvatarUpdate

router = APIRouter(prefix="/avatars", tags=["avatars"])


@router.post("/", response_model=AvatarRead)
def create_avatar(avatar_create: AvatarCreate, db: Session = Depends(get_db)):
    """
    Create a new avatar.

    Parameters:
    - **avatar_create**: AvatarCreate schema containing avatar details.

    Returns:
    - **AvatarRead**: The created avatar data.
    """
    avatar = AvatarService.create_avatar(db, avatar_create)
    return avatar


@router.get("/{wallet_address}", response_model=AvatarRead)
def read_avatar(wallet_address: str, db: Session = Depends(get_db)):
    """
    Retrieve an avatar by wallet address.

    Parameters:
    - **wallet_address**: Ethereum wallet address of the user.

    Returns:
    - **AvatarRead**: The avatar data.
    """
    avatar = AvatarService.get_avatar(db, wallet_address)
    if avatar is None:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar


@router.put("/{wallet_address}", response_model=AvatarRead)
def update_avatar(wallet_address: str, avatar_update: AvatarUpdate, db: Session = Depends(get_db)):
    """
    Update an existing avatar.

    Parameters:
    - **wallet_address**: Ethereum wallet address of the user.
    - **avatar_update**: AvatarUpdate schema with fields to update.

    Returns:
    - **AvatarRead**: The updated avatar data.
    """
    avatar = AvatarService.update_avatar(db, wallet_address, avatar_update)
    if avatar is None:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar


@router.delete("/{wallet_address}", response_model=dict)
def delete_avatar(wallet_address: str, db: Session = Depends(get_db)):
    """
    Delete an avatar by wallet address.

    Parameters:
    - **wallet_address**: Ethereum wallet address of the user.

    Returns:
    - **dict**: A message indicating the deletion status.
    """
    result = AvatarService.delete_avatar(db, wallet_address)
    if not result:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return {"detail": "Avatar deleted successfully"}
