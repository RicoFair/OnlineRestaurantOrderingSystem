from decimal import Decimal
from .common import ORMBase

class RecipeCreate(ORMBase):
    menu_item_id: int
    resource_id: int
    qty: Decimal

class RecipeOut(ORMBase):
    id: int
    menu_item_id: int
    resource_id: int
    qty: Decimal
