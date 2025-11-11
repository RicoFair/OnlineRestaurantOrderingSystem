from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
