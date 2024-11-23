from sqlalchemy.orm import Session
from typing import Optional

from app.models.item import Item as ItemModel
from app.schemas.item import ItemCreate, ItemUpdate
from app.api.repositories.item import ItemRepository


class ItemService:
    """
    Service class for Item model.
    Handles business logic and uses ItemRepository for database operations.
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
        return ItemRepository.get_item(db, item_id)

    @staticmethod
    def create_item(db: Session, item_create: ItemCreate) -> ItemModel:
        """
        Create a new item.

        Args:
            db (Session): Database session.
            item_create (ItemCreate): Data for creating a new item.

        Returns:
            ItemModel: The newly created item model instance.

        Raises:
            ValueError: If the item already exists.
        """
        existing_item = ItemRepository.get_item(db, item_create.item_id)
        if existing_item:
            raise ValueError("Item already exists")
        return ItemRepository.create_item(db, item_create)

    @staticmethod
    def update_item(db: Session, item_id: str, item_update: ItemUpdate) -> Optional[ItemModel]:
        """
        Update an existing item.

        Args:
            db (Session): Database session.
            item_id (str): Item ID.
            item_update (ItemUpdate): Data for updating the item.

        Returns:
            Optional[ItemModel]: Updated item model instance or None if not found.
        """
        db_item = ItemRepository.get_item(db, item_id)
        if not db_item:
            return None
        return ItemRepository.update_item(db, db_item, item_update)

    @staticmethod
    def delete_item(db: Session, item_id: str) -> bool:
        """
        Delete an item.

        Args:
            db (Session): Database session.
            item_id (str): Item ID.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        db_item = ItemRepository.get_item(db, item_id)
        if not db_item:
            return False
        ItemRepository.delete_item(db, db_item)
        return True
