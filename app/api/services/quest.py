from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID

from app.models.quest import Quest as QuestModel
from app.schemas.quest import QuestCreate, QuestUpdate
from app.api.repositories.quest import QuestRepository


class QuestService:
    """
    Service class for Quest model.
    Handles business logic and uses QuestRepository for database operations.
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
        return QuestRepository.get_quest(db, quest_id)
    
    @staticmethod
    def get_quests(db: Session) -> list[QuestModel]:
        """
        Retrieve all quests.

        Args:
            db (Session): Database session.

        Returns:
            list[QuestModel]: List of all quest model instances.
        """
        return QuestRepository.get_quests(db)

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
        return QuestRepository.create_quest(db, quest_create)

    @staticmethod
    def update_quest(db: Session, quest_id: UUID, quest_update: QuestUpdate) -> Optional[QuestModel]:
        """
        Update an existing quest.

        Args:
            db (Session): Database session.
            quest_id (UUID): Quest ID.
            quest_update (QuestUpdate): Data for updating the quest.

        Returns:
            Optional[QuestModel]: Updated quest model instance or None if not found.
        """
        db_quest = QuestRepository.get_quest(db, quest_id)
        if not db_quest:
            return None
        return QuestRepository.update_quest(db, db_quest, quest_update)

    @staticmethod
    def delete_quest(db: Session, quest_id: UUID) -> bool:
        """
        Delete a quest.

        Args:
            db (Session): Database session.
            quest_id (UUID): Quest ID.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        db_quest = QuestRepository.get_quest(db, quest_id)
        if not db_quest:
            return False
        QuestRepository.delete_quest(db, db_quest)
        return True
