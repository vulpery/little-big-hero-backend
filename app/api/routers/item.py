from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.services.item import ItemService
from app.core.database import get_db
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemRead)
def create_item(item_create: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    Parameters:
    - **item_create**: ItemCreate schema containing item details.

    Returns:
    - **ItemRead**: The created item data.
    """
    item = ItemService.create_item(db, item_create)
    return item


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id: str, db: Session = Depends(get_db)):
    """
    Retrieve an item by its ID.

    Parameters:
    - **item_id**: ID of the item.

    Returns:
    - **ItemRead**: The item data.
    """
    item = ItemService.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=ItemRead)
def update_item(item_id: str, item_update: ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an existing item.

    Parameters:
    - **item_id**: ID of the item.
    - **item_update**: ItemUpdate schema with fields to update.

    Returns:
    - **ItemRead**: The updated item data.
    """
    item = ItemService.update_item(db, item_id, item_update)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", response_model=dict)
def delete_item(item_id: str, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.

    Parameters:
    - **item_id**: ID of the item.

    Returns:
    - **dict**: A message indicating the deletion status.
    """
    result = ItemService.delete_item(db, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted successfully"}
