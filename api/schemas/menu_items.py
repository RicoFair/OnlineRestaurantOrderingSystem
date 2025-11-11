from typing import Optional
from decimal import Decimal
from .common import ORMBase

class MenuItemCreate(ORMBase):
    name: str
    price: Decimal
    category_id: Optional[int] = None
    description: Optional[str] = None
    calories: Optional[int] = None
    tags: Optional[str] = None

class MenuItemOut(ORMBase):
    id: int
    name: str
    price: Decimal
    category_id: Optional[int]
    description: Optional[str]
    calories: Optional[int]
    tags: Optional[str]
