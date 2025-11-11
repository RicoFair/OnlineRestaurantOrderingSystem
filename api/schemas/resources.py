from decimal import Decimal
from .common import ORMBase

class ResourceCreate(ORMBase):
    name: str
    unit: str
    on_hand: Decimal = Decimal("0")

class ResourceOut(ORMBase):
    id: int
    name: str
    unit: str
    on_hand: Decimal
