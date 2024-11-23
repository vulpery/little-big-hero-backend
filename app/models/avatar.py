from sqlalchemy import JSON, Column, DateTime, ForeignKey, String, func

from app.core.database import Base


class Avatar(Base):
    __tablename__ = 'avatars'

    wallet_address = Column(String, ForeignKey('users.wallet_address'), primary_key=True)
    equipped_items = Column(JSON)  # List of item IDs
    cosmetic_details = Column(JSON)
    preferences = Column(JSON)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
