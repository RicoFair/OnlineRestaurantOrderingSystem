from pydantic import BaseModel, Field
from typing import Optional

class ORMBase(BaseModel):
    class Config:
        from_attributes = True  # Pydantic v2: enables orm_mode
