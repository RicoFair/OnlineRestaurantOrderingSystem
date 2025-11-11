# api/schemas/orders.py
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    status: Optional[str] = "pending"
    total_amount: Optional[float] = 0.0

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    status: Optional[str] = None
    total_amount: Optional[float] = None

class OrderRead(OrderBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # FastAPI v1+ / Pydantic v2 friendly

# 👇 This one line satisfies router's `response_model=schema.Order`
class Order(OrderRead):
    pass
