from sqlalchemy.orm import Session
from typing import Optional

from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate
from app.api.repositories.user import UserRepository


class UserService:
    """
    Service class for User model.
    Handles business logic and uses UserRepository for database operations.
    """

    @staticmethod
    def get_user(db: Session, wallet_address: str) -> Optional[UserModel]:
        """
        Retrieve a user by wallet address.
        """
        return UserRepository.get_user(db, wallet_address)

    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> UserModel:
        """
        Create a new user.
        """
        existing_user = UserRepository.get_user(db, user_create.wallet_address)
        if existing_user:
            raise ValueError("User already exists")
        return UserRepository.create_user(db, user_create)

    @staticmethod
    def update_user(db: Session, wallet_address: str, user_update: UserUpdate) -> Optional[UserModel]:
        """
        Update an existing user.
        """
        db_user = UserRepository.get_user(db, wallet_address)
        if not db_user:
            return None
        return UserRepository.update_user(db, db_user, user_update)

    @staticmethod
    def delete_user(db: Session, wallet_address: str) -> bool:
        """
        Delete a user.
        """
        db_user = UserRepository.get_user(db, wallet_address)
        if not db_user:
            return False
        UserRepository.delete_user(db, db_user)
        return True
