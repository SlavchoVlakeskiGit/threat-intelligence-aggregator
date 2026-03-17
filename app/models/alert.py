from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.db.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    matched_value = Column(String(255), nullable=False, index=True)
    indicator_type = Column(String(50), nullable=False)
    severity = Column(String(20), nullable=False, default="medium")
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())