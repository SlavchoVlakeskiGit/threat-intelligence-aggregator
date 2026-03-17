from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.database import Base


class Indicator(Base):
    __tablename__ = "indicators"

    id = Column(Integer, primary_key=True, index=True)
    indicator_type = Column(String(50), nullable=False)
    value = Column(String(255), nullable=False, unique=True, index=True)
    source_name = Column(String(100), nullable=False)
    confidence_score = Column(Integer, nullable=False, default=50)
    created_at = Column(DateTime(timezone=True), server_default=func.now())