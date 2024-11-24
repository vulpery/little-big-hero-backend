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
        """
        return (
            db.query(UserModel)
            .filter(UserModel.wallet_address == wallet_address)
            .first()
        )

    @staticmethod
    def get_users(db: Session) -> list[UserModel]:
        """
        Retrieve all users.
        """
        return db.query(UserModel).all()

    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> UserModel:
        """
        Create a new user.
        """
        db_user = UserModel(**user_create.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(
        db: Session, db_user: UserModel, user_update: UserUpdate
    ) -> UserModel:
        """
        Update an existing user.
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
        """
        db.delete(db_user)
        db.commit()
