import enum
import uuid

from sqlalchemy import JSON, Column, DateTime, Enum, ForeignKey, String, func, Float
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class QuestStatus(enum.Enum):
    available = "available"
    accepted = "accepted"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"


class Quest(Base):
    __tablename__ = 'quests'

    quest_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    creator_wallet = Column(String, ForeignKey('users.wallet_address'))
    participant_wallet = Column(String, ForeignKey('users.wallet_address'), nullable=True)
    title = Column(String)
    description = Column(String)
    location = Column(String)
    longitude = Column(Float, nullable=False)  # Longitude of the location
    latitude = Column(Float, nullable=False)  # Latitude of the location
    time_window = Column(JSON)  # Store start and end times as JSON
    rewards = Column(JSON)      # Store EXP and items as JSON
    status = Column(Enum(QuestStatus), default=QuestStatus.available)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
