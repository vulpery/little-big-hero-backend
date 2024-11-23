from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """
    Base schema for Item, containing common fields.

    Example:
        {
            "name": "Sword of Truth",
            "description": "A legendary sword with immense power.",
            "attributes": {
                "damage": 100,
                "durability": 250
            },
            "image_url": "https://example.com/items/sword_of_truth.png",
            "metadata_uri": "https://metadata.example.com/items/sword_of_truth.json"
        }
    """
    name: str = Field(..., example="Sword of Truth", description="Name of the item.")
    description: str = Field(..., example="A legendary sword with immense power.", description="Description of the item.")
    attributes: Dict[str, Any] = Field(..., example={"damage": 100, "durability": 250}, description="Custom attributes of the item.")
    image_url: Optional[str] = Field(None, example="https://example.com/items/sword_of_truth.png", description="URL of the item's image.")
    metadata_uri: Optional[str] = Field(None, example="https://metadata.example.com/items/sword_of_truth.json", description="Metadata URI for additional details about the item.")


class ItemCreate(ItemBase):
    """
    Schema for creating a new item.

    Example:
        {
            "item_id": "sword_of_truth",
            "owner_wallet": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
            "name": "Sword of Truth",
            "description": "A legendary sword with immense power.",
            "attributes": {
                "damage": 100,
                "durability": 250
            },
            "image_url": "https://example.com/items/sword_of_truth.png",
            "metadata_uri": "https://metadata.example.com/items/sword_of_truth.json"
        }
    """
    item_id: str = Field(..., example="sword_of_truth", description="Unique identifier for the item.")
    owner_wallet: str = Field(..., example="0xabcdefabcdefabcdefabcdefabcdefabcdef", description="Wallet address of the item's owner.")


class ItemUpdate(BaseModel):
    """
    Schema for updating an existing item.

    Example:
        {
            "name": "Enhanced Sword of Truth",
            "description": "An upgraded legendary sword.",
            "attributes": {
                "damage": 150,
                "durability": 300
            },
            "image_url": "https://example.com/items/enhanced_sword_of_truth.png",
            "metadata_uri": "https://metadata.example.com/items/enhanced_sword_of_truth.json"
        }
    """
    name: Optional[str] = Field(None, example="Enhanced Sword of Truth", description="Updated name of the item.")
    description: Optional[str] = Field(None, example="An upgraded legendary sword.", description="Updated description of the item.")
    attributes: Optional[Dict[str, Any]] = Field(None, example={"damage": 150, "durability": 300}, description="Updated attributes of the item.")
    image_url: Optional[str] = Field(None, example="https://example.com/items/enhanced_sword_of_truth.png", description="Updated URL of the item's image.")
    metadata_uri: Optional[str] = Field(None, example="https://metadata.example.com/items/enhanced_sword_of_truth.json", description="Updated metadata URI for the item.")


class ItemRead(ItemBase):
    """
    Schema for reading item data.

    Example:
        {
            "item_id": "sword_of_truth",
            "owner_wallet": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
            "name": "Sword of Truth",
            "description": "A legendary sword with immense power.",
            "attributes": {
                "damage": 100,
                "durability": 250
            },
            "image_url": "https://example.com/items/sword_of_truth.png",
            "metadata_uri": "https://metadata.example.com/items/sword_of_truth.json",
            "created_at": "2023-01-05T14:00:00Z",
            "updated_at": "2023-01-10T16:30:00Z"
        }
    """
    item_id: str = Field(..., example="sword_of_truth", description="Unique identifier for the item.")
    owner_wallet: str = Field(..., example="0xabcdefabcdefabcdefabcdefabcdefabcdef", description="Wallet address of the item's owner.")
    created_at: Optional[datetime] = Field(None, example="2023-01-05T14:00:00Z", description="Timestamp when the item was created.")
    updated_at: Optional[datetime] = Field(None, example="2023-01-10T16:30:00Z", description="Timestamp when the item was last updated.")

    class Config:
        orm_mode = True
        json_encoders = {datetime: lambda v: v.isoformat()}


class ItemDelete(BaseModel):
    """
    Schema for deleting an item.

    Example:
        {
            "item_id": "sword_of_truth"
        }
    """
    item_id: str = Field(..., example="sword_of_truth", description="Unique identifier of the item to be deleted.")
