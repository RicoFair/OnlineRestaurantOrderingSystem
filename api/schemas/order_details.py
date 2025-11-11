# api/schemas/order_details.py
from typing import Optional
from pydantic import BaseModel

# ---- Shared fields for an order line item ----
class OrderDetailBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int = 1
    unit_price: float = 0.0
    line_total: Optional[float] = None  # can be computed as quantity * unit_price

# ---- Create ----
class OrderDetailCreate(OrderDetailBase):
    pass

# ---- Update (all optional so we can PATCH/PUT) ----
class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    quantity: Optional[int] = None
    unit_price: Optional[float] = None
    line_total: Optional[float] = None

# ---- Read (what we send back to clients) ----
class OrderDetailRead(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True  # pydantic v2 / SQLAlchemy compatibility

# 👇 Matches router's `response_model=schema.OrderDetail`
class OrderDetail(OrderDetailRead):
    pass
