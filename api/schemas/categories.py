from .common import ORMBase

class CategoryCreate(ORMBase):
    name: str

class CategoryOut(ORMBase):
    id: int
    name: str
