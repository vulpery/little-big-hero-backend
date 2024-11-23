from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class QuestStatus(str, Enum):
    """
    Enumeration of possible quest statuses.

    Values:
        - available
        - in_progress
        - completed
        - cancelled
    """
    available = "available"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class TimeWindow(BaseModel):
    """
    Represents the time window for a quest.

    Example:
        {
            "start_time": "2023-01-15T09:00:00Z",
            "end_time": "2023-01-15T17:00:00Z"
        }
    """
    start_time: datetime = Field(..., example="2023-01-15T09:00:00Z")
    end_time: datetime = Field(..., example="2023-01-15T17:00:00Z")

    class Config:
        orm_mode = True


class Rewards(BaseModel):
    """
    Represents the rewards for completing a quest.

    Example:
        {
            "experience_points": 500,
            "items": ["sword_of_truth", "shield_of_valor"]
        }
    """
    experience_points: int = Field(..., example=500)
    items: List[str] = Field(..., example=["sword_of_truth", "shield_of_valor"])


class QuestBase(BaseModel):
    """
    Base schema for Quest, containing common fields.

    Example:
        {
            "title": "Defeat the Dragon",
            "description": "Slay the dragon terrorizing the village.",
            "location": "Dragon's Lair",
            "time_window": {
                "start_time": "2023-01-20T08:00:00Z",
                "end_time": "2023-01-20T18:00:00Z"
            },
            "rewards": {
                "experience_points": 1000,
                "items": ["dragon_scale_armor"]
            }
        }
    """
    title: str = Field(..., example="Defeat the Dragon")
    description: str = Field(..., example="Slay the dragon terrorizing the village.")
    location: str = Field(..., example="Dragon's Lair")
    time_window: TimeWindow
    rewards: Rewards

    class Config:
        orm_mode = True


class QuestCreate(QuestBase):
    """
    Schema for creating a new quest.

    Example:
        {
            "creator_wallet": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
            "title": "Defeat the Dragon",
            "description": "Slay the dragon terrorizing the village.",
            "location": "Dragon's Lair",
            "time_window": {
                "start_time": "2023-01-20T08:00:00Z",
                "end_time": "2023-01-20T18:00:00Z"
            },
            "rewards": {
                "experience_points": 1000,
                "items": ["dragon_scale_armor"]
            }
        }
    """
    creator_wallet: str = Field(..., example="0xabcdefabcdefabcdefabcdefabcdefabcdef")


class QuestUpdate(BaseModel):
    """
    Schema for updating an existing quest.

    Example:
        {
            "participant_wallet": "0x1234567890abcdef1234567890abcdef12345678",
            "title": "Defeat the Dragon Quickly",
            "description": "Slay the dragon before sunset.",
            "location": "Dragon's Lair",
            "time_window": {
                "start_time": "2023-01-20T06:00:00Z",
                "end_time": "2023-01-20T12:00:00Z"
            },
            "rewards": {
                "experience_points": 1500,
                "items": ["dragon_scale_armor", "ring_of_speed"]
            },
            "status": "in_progress"
        }
    """
    participant_wallet: Optional[str] = Field(None, example="0x1234567890abcdef1234567890abcdef12345678")
    title: Optional[str] = Field(None, example="Defeat the Dragon Quickly")
    description: Optional[str] = Field(None, example="Slay the dragon before sunset.")
    location: Optional[str] = Field(None, example="Dragon's Lair")
    time_window: Optional[TimeWindow] = None
    rewards: Optional[Rewards] = None
    status: Optional[QuestStatus] = Field(None, example="in_progress")

    class Config:
        orm_mode = True


class QuestRead(QuestBase):
    """
    Schema for reading quest data.

    Example:
        {
            "quest_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "creator_wallet": "0xabcdefabcdefabcdefabcdefabcdefabcdef",
            "participant_wallet": "0x1234567890abcdef1234567890abcdef12345678",
            "title": "Defeat the Dragon",
            "description": "Slay the dragon terrorizing the village.",
            "location": "Dragon's Lair",
            "time_window": {
                "start_time": "2023-01-20T08:00:00Z",
                "end_time": "2023-01-20T18:00:00Z"
            },
            "rewards": {
                "experience_points": 1000,
                "items": ["dragon_scale_armor"]
            },
            "status": "available",
            "created_at": "2023-01-10T10:00:00Z",
            "updated_at": "2023-01-12T12:00:00Z"
        }
    """
    quest_id: UUID = Field(..., example="f47ac10b-58cc-4372-a567-0e02b2c3d479")
    creator_wallet: str = Field(..., example="0xabcdefabcdefabcdefabcdefabcdefabcdef")
    participant_wallet: Optional[str] = Field(None, example="0x1234567890abcdef1234567890abcdef12345678")
    status: QuestStatus = Field(..., example="available")
    created_at: Optional[datetime] = Field(None, example="2023-01-10T10:00:00Z")
    updated_at: Optional[datetime] = Field(None, example="2023-01-12T12:00:00Z")

    class Config:
        orm_mode = True
        json_encoders = {datetime: lambda v: v.isoformat()}


class QuestDelete(BaseModel):
    """
    Schema for deleting a quest.

    Example:
        {
            "quest_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
        }
    """
    quest_id: UUID = Field(..., example="f47ac10b-58cc-4372-a567-0e02b2c3d479")
