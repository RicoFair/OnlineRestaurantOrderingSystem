from sqlalchemy import Column, Integer, String, Numeric
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    unit = Column(String(30), nullable=False)     # 'g','ml','pcs'
    on_hand = Column(Numeric(12,3), nullable=False, default=0)
