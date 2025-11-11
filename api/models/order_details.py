from sqlalchemy import Column, Integer, Numeric, ForeignKey
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id", ondelete="SET NULL"), nullable=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10,2), nullable=False)
    line_total = Column(Numeric(10,2), nullable=False)
