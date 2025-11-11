from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=schema.Order, status_code=status.HTTP_201_CREATED)
def create_order(payload: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=payload)


@router.get("/", response_model=list[schema.Order])
def list_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Order)
def get_order(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update_order(item_id: int, payload: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=payload, item_id=item_id)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(item_id: int, db: Session = Depends(get_db)):
    controller.delete(db=db, item_id=item_id)
    return None
