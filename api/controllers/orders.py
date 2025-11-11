from __future__ import annotations

from typing import List, Optional
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models.orders import Order as OrderModel
from ..schemas.orders import OrderCreate, OrderUpdate


# ---------- Create ----------
def create(db: Session, request: OrderCreate) -> OrderModel:
    obj = OrderModel(
        tracking_no=str(uuid4())[:8],   # simple short tracking code
        status=request.status,
        total_price=request.total_price,
    )
    if request.customer_id is not None:
        obj.customer_id = request.customer_id

    db.add(obj)
    try:
        db.commit()
        db.refresh(obj)
        return obj
    except IntegrityError:
        db.rollback()
        # Usually means invalid customer_id (FK) or unique tracking clash
        raise HTTPException(status_code=400, detail="Invalid data (e.g., customer_id does not exist).")


# ---------- Read all ----------
def read_all(db: Session) -> List[OrderModel]:
    return db.query(OrderModel).order_by(OrderModel.id.desc()).all()


# ---------- Read one ----------
def read_one(db: Session, item_id: int) -> OrderModel:
    obj: Optional[OrderModel] = db.query(OrderModel).get(item_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return obj


# ---------- Update ----------
def update(db: Session, request: OrderUpdate, item_id: int) -> OrderModel:
    obj: Optional[OrderModel] = db.query(OrderModel).get(item_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

    # Apply only provided fields
    if request.status is not None:
        obj.status = request.status
    if request.customer_id is not None:
        obj.customer_id = request.customer_id
    if request.total_price is not None:
        obj.total_price = request.total_price

    try:
        db.commit()
        db.refresh(obj)
        return obj
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid data (e.g., customer_id does not exist).")


# ---------- Delete ----------
def delete(db: Session, item_id: int) -> dict:
    obj: Optional[OrderModel] = db.query(OrderModel).get(item_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    db.delete(obj)
    db.commit()
    return {"ok": True}
