from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# What the client can send (and what we re-use for responses)
class OrderBase(BaseModel):
    status: str = Field(default="pending")           # pending / preparing / ready / delivered
    customer_id: Optional[int] = None                # optional FK
    total_price: float = 0.0                         # float on the API to avoid Decimal JSON issues


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    customer_id: Optional[int] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    tracking_no: str
    ordered_at: datetime

    class Config:
        from_attributes = True   # allow reading from SQLAlchemy objects
