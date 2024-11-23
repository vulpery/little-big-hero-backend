from sqlalchemy.orm import Session
from typing import Optional

from app.models.avatar import Avatar as AvatarModel
from app.schemas.avatar import AvatarCreate, AvatarUpdate
from app.api.repositories.avatar import AvatarRepository


class AvatarService:
    """
    Service class for Avatar model.
    Handles business logic and uses AvatarRepository for database operations.
    """

    @staticmethod
    def get_avatar(db: Session, wallet_address: str) -> Optional[AvatarModel]:
        """
        Retrieve an avatar by wallet address.

        Args:
            db (Session): Database session.
            wallet_address (str): User's wallet address.

        Returns:
            Optional[AvatarModel]: Avatar model instance or None if not found.
        """
        return AvatarRepository.get_avatar(db, wallet_address)

    @staticmethod
    def create_avatar(db: Session, avatar_create: AvatarCreate) -> AvatarModel:
        """
        Create a new avatar.

        Args:
            db (Session): Database session.
            avatar_create (AvatarCreate): Data for creating a new avatar.

        Returns:
            AvatarModel: The newly created avatar model instance.

        Raises:
            ValueError: If the avatar already exists.
        """
        existing_avatar = AvatarRepository.get_avatar(db, avatar_create.wallet_address)
        if existing_avatar:
            raise ValueError("Avatar already exists")
        return AvatarRepository.create_avatar(db, avatar_create)

    @staticmethod
    def update_avatar(db: Session, wallet_address: str, avatar_update: AvatarUpdate) -> Optional[AvatarModel]:
        """
        Update an existing avatar.

        Args:
            db (Session): Database session.
            wallet_address (str): User's wallet address.
            avatar_update (AvatarUpdate): Data for updating the avatar.

        Returns:
            Optional[AvatarModel]: Updated avatar model instance or None if not found.
        """
        db_avatar = AvatarRepository.get_avatar(db, wallet_address)
        if not db_avatar:
            return None
        return AvatarRepository.update_avatar(db, db_avatar, avatar_update)

    @staticmethod
    def delete_avatar(db: Session, wallet_address: str) -> bool:
        """
        Delete an avatar.

        Args:
            db (Session): Database session.
            wallet_address (str): User's wallet address.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        db_avatar = AvatarRepository.get_avatar(db, wallet_address)
        if not db_avatar:
            return False
        AvatarRepository.delete_avatar(db, db_avatar)
        return True
