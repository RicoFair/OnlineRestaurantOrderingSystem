from typing import Optional
from .common import ORMBase

class PaymentCreate(ORMBase):
    order_id: int
    type: str
    status: str
    txn_id: Optional[str] = None

class PaymentOut(ORMBase):
    id: int
    order_id: int
    type: str
    status: str
    txn_id: Optional[str]
