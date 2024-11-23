from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.services.quest import QuestService
from app.core.database import get_db
from app.schemas.quest import QuestCreate, QuestRead, QuestUpdate

router = APIRouter(prefix="/quests", tags=["quests"])


@router.post("/", response_model=QuestRead)
def create_quest(quest_create: QuestCreate, db: Session = Depends(get_db)):
    """
    Create a new quest.

    Parameters:
    - **quest_create**: QuestCreate schema containing quest details.

    Returns:
    - **QuestRead**: The created quest data.
    """
    quest = QuestService.create_quest(db, quest_create)
    return quest


@router.get("/{quest_id}", response_model=QuestRead)
def read_quest(quest_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a quest by its ID.

    Parameters:
    - **quest_id**: UUID of the quest.

    Returns:
    - **QuestRead**: The quest data.
    """
    quest = QuestService.get_quest(db, quest_id)
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest


@router.put("/{quest_id}", response_model=QuestRead)
def update_quest(quest_id: str, quest_update: QuestUpdate, db: Session = Depends(get_db)):
    """
    Update an existing quest.

    Parameters:
    - **quest_id**: UUID of the quest.
    - **quest_update**: QuestUpdate schema with fields to update.

    Returns:
    - **QuestRead**: The updated quest data.
    """
    quest = QuestService.update_quest(db, quest_id, quest_update)
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest


@router.delete("/{quest_id}", response_model=dict)
def delete_quest(quest_id: str, db: Session = Depends(get_db)):
    """
    Delete a quest by its ID.

    Parameters:
    - **quest_id**: UUID of the quest.

    Returns:
    - **dict**: A message indicating the deletion status.
    """
    result = QuestService.delete_quest(db, quest_id)
    if not result:
        raise HTTPException(status_code=404, detail="Quest not found")
    return {"detail": "Quest deleted successfully"}
