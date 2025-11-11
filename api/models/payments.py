from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    type = Column(String(20), nullable=False)   # card, cash, applepay ...
    status = Column(String(20), nullable=False) # authorized, settled, failed
    txn_id = Column(String(100), nullable=True)
