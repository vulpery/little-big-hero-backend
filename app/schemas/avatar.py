from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AvatarBase(BaseModel):
    """
    Base schema for Avatar, containing common fields.

    Example:
        {
            "equipped_items": ["sword_of_truth", "shield_of_valor"],
            "cosmetic_details": {
                "hair_color": "blonde",
                "eye_color": "blue"
            },
            "preferences": {
                "theme": "dark",
                "notifications": True
            }
        }
    """
    equipped_items: List[str] = Field(..., example=["sword_of_truth", "shield_of_valor"])
    cosmetic_details: Dict[str, Any] = Field(..., example={"hair_color": "blonde", "eye_color": "blue"})
    preferences: Dict[str, Any] = Field(..., example={"theme": "dark", "notifications": True})


class AvatarCreate(AvatarBase):
    """
    Schema for creating a new avatar.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "equipped_items": ["sword_of_truth", "shield_of_valor"],
            "cosmetic_details": {
                "hair_color": "blonde",
                "eye_color": "blue"
            },
            "preferences": {
                "theme": "dark",
                "notifications": True
            }
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")


class AvatarUpdate(BaseModel):
    """
    Schema for updating an existing avatar.

    Example:
        {
            "equipped_items": ["enhanced_sword_of_truth", "dragon_shield"],
            "cosmetic_details": {
                "hair_color": "black",
                "eye_color": "green"
            },
            "preferences": {
                "theme": "light",
                "notifications": False
            }
        }
    """
    equipped_items: Optional[List[str]] = Field(None, example=["enhanced_sword_of_truth", "dragon_shield"])
    cosmetic_details: Optional[Dict[str, Any]] = Field(None, example={"hair_color": "black", "eye_color": "green"})
    preferences: Optional[Dict[str, Any]] = Field(None, example={"theme": "light", "notifications": False})


class AvatarRead(AvatarBase):
    """
    Schema for reading avatar data.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678",
            "equipped_items": ["sword_of_truth", "shield_of_valor"],
            "cosmetic_details": {
                "hair_color": "blonde",
                "eye_color": "blue"
            },
            "preferences": {
                "theme": "dark",
                "notifications": True
            },
            "updated_at": "2023-01-15T18:45:00Z"
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")
    updated_at: Optional[datetime] = Field(None, example="2023-01-15T18:45:00Z")


class AvatarDelete(BaseModel):
    """
    Schema for deleting an avatar.

    Example:
        {
            "wallet_address": "0x1234567890abcdef1234567890abcdef12345678"
        }
    """
    wallet_address: str = Field(..., example="0x1234567890abcdef1234567890abcdef12345678")
