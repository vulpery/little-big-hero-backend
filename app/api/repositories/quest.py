import operator
from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID

from app.models.quest import Quest as QuestModel
from app.schemas.quest import QuestCreate, QuestUpdate


class QuestRepository:
    """
    Repository class for Quest model.
    Handles all database operations related to Quest.
    """

    @staticmethod
    def get_quest(db: Session, quest_id: UUID) -> Optional[QuestModel]:
        """
        Retrieve a quest by ID.

        Args:
            db (Session): Database session.
            quest_id (UUID): Quest ID.

        Returns:
            Optional[QuestModel]: Quest model instance or None if not found.
        """
        return db.query(QuestModel).filter(operator.eq(QuestModel.quest_id,quest_id)).first()

    @staticmethod
    def create_quest(db: Session, quest_create: QuestCreate) -> QuestModel:
        """
        Create a new quest.

        Args:
            db (Session): Database session.
            quest_create (QuestCreate): Data for creating a new quest.

        Returns:
            QuestModel: The newly created quest model instance.
        """
        db_quest = QuestModel(**quest_create.dict())
        db.add(db_quest)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    @staticmethod
    def update_quest(db: Session, db_quest: QuestModel, quest_update: QuestUpdate) -> QuestModel:
        """
        Update an existing quest.

        Args:
            db (Session): Database session.
            db_quest (QuestModel): The quest model instance to update.
            quest_update (QuestUpdate): Data for updating the quest.

        Returns:
            QuestModel: The updated quest model instance.
        """
        for key, value in quest_update.dict(exclude_unset=True).items():
            setattr(db_quest, key, value)
        db.commit()
        db.refresh(db_quest)
        return db_quest

    @staticmethod
    def delete_quest(db: Session, db_quest: QuestModel) -> None:
        """
        Delete a quest.

        Args:
            db (Session): Database session.
            db_quest (QuestModel): The quest model instance to delete.
        """
        db.delete(db_quest)
        db.commit()
