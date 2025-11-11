from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    tracking_no = Column(String(40), unique=True, index=True, nullable=False)
    status = Column(String(20), nullable=False, default="pending")  # pending/preparing/ready/delivered
    ordered_at = Column(DateTime(timezone=True), server_default=func.now())
    customer_id = Column(Integer, ForeignKey("customers.id", ondelete="SET NULL"), nullable=True)
    total_price = Column(Numeric(10,2), nullable=False, default=0)
    customer = relationship("Customer")
