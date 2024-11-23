import operator
from sqlalchemy.orm import Session
from typing import Optional

from app.models.avatar import Avatar as AvatarModel
from app.schemas.avatar import AvatarCreate, AvatarUpdate


class AvatarRepository:
    """
    Repository class for Avatar model.
    Handles all database operations related to Avatar.
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
        return db.query(AvatarModel).filter(AvatarModel.wallet_address == wallet_address).first()

    @staticmethod
    def create_avatar(db: Session, avatar_create: AvatarCreate) -> AvatarModel:
        """
        Create a new avatar.

        Args:
            db (Session): Database session.
            avatar_create (AvatarCreate): Data for creating a new avatar.

        Returns:
            AvatarModel: The newly created avatar model instance.
        """
        db_avatar = AvatarModel(**avatar_create.dict())
        db.add(db_avatar)
        db.commit()
        db.refresh(db_avatar)
        return db_avatar

    @staticmethod
    def update_avatar(db: Session, db_avatar: AvatarModel, avatar_update: AvatarUpdate) -> AvatarModel:
        """
        Update an existing avatar.

        Args:
            db (Session): Database session.
            db_avatar (AvatarModel): The avatar model instance to update.
            avatar_update (AvatarUpdate): Data for updating the avatar.

        Returns:
            AvatarModel: The updated avatar model instance.
        """
        for key, value in avatar_update.dict(exclude_unset=True).items():
            setattr(db_avatar, key, value)
        db.commit()
        db.refresh(db_avatar)
        return db_avatar

    @staticmethod
    def delete_avatar(db: Session, db_avatar: AvatarModel) -> None:
        """
        Delete an avatar.

        Args:
            db (Session): Database session.
            db_avatar (AvatarModel): The avatar model instance to delete.
        """
        db.delete(db_avatar)
        db.commit()
