from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id", ondelete="CASCADE"), nullable=False)
    score = Column(Integer, nullable=False)  # 1..5
    text = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
