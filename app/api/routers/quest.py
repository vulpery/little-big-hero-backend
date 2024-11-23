from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.services.quest import QuestService
from app.core.database import get_db
from app.schemas.quest import QuestCreate, QuestRead, QuestUpdate

router = APIRouter(
    prefix="/quests",
    tags=["Quests"],
    responses={404: {"description": "Not Found"}},
)


@router.post("/", response_model=QuestRead, summary="Create a new quest", description="Create a quest by providing details using the QuestCreate schema.")
def create_quest(quest_create: QuestCreate, db: Session = Depends(get_db)):
    """
    **Create a new quest**.

    **Parameters:**
    - **quest_create** (*QuestCreate*): A schema containing the quest details such as title, description, and rewards.

    **Returns:**
    - **QuestRead** (*QuestRead*): The newly created quest data.
    """
    quest = QuestService.create_quest(db, quest_create)
    return quest


@router.get("/{quest_id}", response_model=QuestRead, summary="Retrieve quest details", description="Retrieve details of a specific quest by providing its UUID.")
def read_quest(quest_id: str, db: Session = Depends(get_db)):
    """
    **Retrieve a quest by its ID**.

    **Parameters:**
    - **quest_id** (*str*): The UUID of the quest.

    **Returns:**
    - **QuestRead** (*QuestRead*): The quest data if found.

    **Raises:**
    - **404 Not Found**: If the quest with the specified UUID does not exist.
    """
    quest = QuestService.get_quest(db, quest_id)
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest


@router.put("/{quest_id}", response_model=QuestRead, summary="Update an existing quest", description="Update the details of a specific quest by providing its UUID and update data.")
def update_quest(quest_id: str, quest_update: QuestUpdate, db: Session = Depends(get_db)):
    """
    **Update an existing quest**.

    **Parameters:**
    - **quest_id** (*str*): The UUID of the quest to update.
    - **quest_update** (*QuestUpdate*): A schema containing the fields to update.

    **Returns:**
    - **QuestRead** (*QuestRead*): The updated quest data.

    **Raises:**
    - **404 Not Found**: If the quest with the specified UUID does not exist.
    """
    quest = QuestService.update_quest(db, quest_id, quest_update)
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest


@router.delete("/{quest_id}", response_model=dict, summary="Delete a quest", description="Delete a specific quest by providing its UUID.")
def delete_quest(quest_id: str, db: Session = Depends(get_db)):
    """
    **Delete a quest by its ID**.

    **Parameters:**
    - **quest_id** (*str*): The UUID of the quest to delete.

    **Returns:**
    - **dict**: A message indicating the deletion status.

    **Raises:**
    - **404 Not Found**: If the quest with the specified UUID does not exist.
    """
    result = QuestService.delete_quest(db, quest_id)
    if not result:
        raise HTTPException(status_code=404, detail="Quest not found")
    return {"detail": "Quest deleted successfully"}
