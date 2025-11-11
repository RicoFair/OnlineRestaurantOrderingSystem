from sqlalchemy import Column, Integer, Numeric, ForeignKey
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id", ondelete="CASCADE"), nullable=False)
    resource_id  = Column(Integer, ForeignKey("resources.id", ondelete="CASCADE"), nullable=False)
    qty = Column(Numeric(12,3), nullable=False)
