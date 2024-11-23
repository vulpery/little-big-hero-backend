from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """
    Base schema for User, containing common fields.

    Example:
        {
            "username": "john_doe",
            "email": "john@example.com",
            "avatar_image": "https://example.com/avatar.jpg"
        }
    """
    username: Optional[str] = Field(None, example="john_doe")
    email: Optional[str] = Field(None, example="john@example.com")
    avatar_image: Optional[str] = Field(None, example="https://example.com/avatar.jpg")


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "username": "john_doe",
            "email": "john@example.com",
            "avatar_image": "https://example.com/avatar.jpg"
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")


class UserUpdate(BaseModel):
    """
    Schema for updating an existing user.

    Example:
        {
            "username": "jane_doe",
            "email": "jane@example.com",
            "avatar_image": "https://example.com/new_avatar.jpg",
            "experience_points": 2000,
            "level": 6
        }
    """
    username: Optional[str] = Field(None, example="jane_doe")
    email: Optional[str] = Field(None, example="jane@example.com")
    avatar_image: Optional[str] = Field(None, example="https://example.com/new_avatar.jpg")
    experience_points: Optional[int] = Field(None, example=2000)
    level: Optional[int] = Field(None, example=6)


class UserRead(UserBase):
    """
    Schema for reading user data.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "username": "john_doe",
            "email": "john@example.com",
            "avatar_image": "https://example.com/avatar.jpg",
            "experience_points": 1500,
            "level": 5,
            "created_at": "2023-01-01T12:00:00Z",
            "updated_at": "2023-01-10T15:30:00Z"
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")
    experience_points: int = Field(0, example=1500)
    level: int = Field(1, example=5)
    created_at: Optional[datetime] = Field(None, example="2023-01-01T12:00:00Z")
    updated_at: Optional[datetime] = Field(None, example="2023-01-10T15:30:00Z")


class UserDelete(BaseModel):
    """
    Schema for deleting a user.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678"
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")
