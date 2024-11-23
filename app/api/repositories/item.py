import operator
from sqlalchemy.orm import Session
from typing import Optional

from app.models.item import Item as ItemModel
from app.schemas.item import ItemCreate, ItemUpdate


class ItemRepository:
    """
    Repository class for Item model.
    Handles all database operations related to Item.
    """

    @staticmethod
    def get_item(db: Session, item_id: str) -> Optional[ItemModel]:
        """
        Retrieve an item by item ID.

        Args:
            db (Session): Database session.
            item_id (str): Item ID.

        Returns:
            Optional[ItemModel]: Item model instance or None if not found.
        """
        return db.query(ItemModel).filter(operator.eq(ItemModel.item_id, item_id)).first()

    @staticmethod
    def create_item(db: Session, item_create: ItemCreate) -> ItemModel:
        """
        Create a new item.

        Args:
            db (Session): Database session.
            item_create (ItemCreate): Data for creating a new item.

        Returns:
            ItemModel: The newly created item model instance.
        """
        db_item = ItemModel(**item_create.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update_item(db: Session, db_item: ItemModel, item_update: ItemUpdate) -> ItemModel:
        """
        Update an existing item.

        Args:
            db (Session): Database session.
            db_item (ItemModel): The item model instance to update.
            item_update (ItemUpdate): Data for updating the item.

        Returns:
            ItemModel: The updated item model instance.
        """
        for key, value in item_update.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def delete_item(db: Session, db_item: ItemModel) -> None:
        """
        Delete an item.

        Args:
            db (Session): Database session.
            db_item (ItemModel): The item model instance to delete.
        """
        db.delete(db_item)
        db.commit()
