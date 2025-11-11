from typing import Optional
from .common import ORMBase

class ReviewCreate(ORMBase):
    customer_id: int
    menu_item_id: int
    score: int
    text: Optional[str] = None

class ReviewOut(ORMBase):
    id: int
    customer_id: int
    menu_item_id: int
    score: int
    text: Optional[str]
