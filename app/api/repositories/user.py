import operator

from sqlalchemy.orm import Session
from typing import Optional

from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    """
    Repository class for User model.
    Handles all database operations related to User.
    """

    @staticmethod
    def get_user(db: Session, wallet_address: str) -> Optional[UserModel]:
        """
        Retrieve a user by wallet address.

        Args:
            db (Session): Database session.
            wallet_address (str): User's wallet address.

        Returns:
            Optional[UserModel]: User model instance or None if not found.
        """
        return db.query(UserModel).filter(operator.eq(UserModel.wallet_address, wallet_address)).first()

    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> UserModel:
        """
        Create a new user.

        Args:
            db (Session): Database session.
            user_create (UserCreate): Data for creating a new user.

        Returns:
            UserModel: The newly created user model instance.
        """
        db_user = UserModel(**user_create.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, db_user: UserModel, user_update: UserUpdate) -> UserModel:
        """
        Update an existing user.

        Args:
            db (Session): Database session.
            db_user (UserModel): The user model instance to update.
            user_update (UserUpdate): Data for updating the user.

        Returns:
            UserModel: The updated user model instance.
        """
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, db_user: UserModel) -> None:
        """
        Delete a user.

        Args:
            db (Session): Database session.
            db_user (UserModel): The user model instance to delete.
        """
        db.delete(db_user)
        db.commit()
