from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.db.database import Base


class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String(100), nullable=True, index=True)
    domain = Column(String(255), nullable=True, index=True)
    event_type = Column(String(100), nullable=False)
    raw_message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())