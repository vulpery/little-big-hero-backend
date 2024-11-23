from sqlalchemy import JSON, Column, DateTime, ForeignKey, String, func

from app.core.database import Base


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(String, primary_key=True, index=True)
    owner_wallet = Column(String, ForeignKey('users.wallet_address'))
    name = Column(String)
    description = Column(String)
    attributes = Column(JSON)
    image_url = Column(String)
    metadata_uri = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
