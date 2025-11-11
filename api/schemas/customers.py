from typing import Optional
from .common import ORMBase

class CustomerCreate(ORMBase):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerUpdate(ORMBase):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerOut(ORMBase):
    id: int
    name: str
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
