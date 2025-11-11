from sqlalchemy import Column, Integer, String, DateTime, Numeric
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True)
    code = Column(String(40), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=True)
    percent_off = Column(Numeric(5,2), nullable=False)  # e.g., 10.00 = 10%
