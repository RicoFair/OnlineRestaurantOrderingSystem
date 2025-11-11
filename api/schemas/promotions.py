from datetime import datetime
from decimal import Decimal
from .common import ORMBase

class PromotionCreate(ORMBase):
    code: str
    expires_at: datetime | None = None
    percent_off: Decimal

class PromotionOut(ORMBase):
    id: int
    code: str
    expires_at: datetime | None
    percent_off: Decimal
