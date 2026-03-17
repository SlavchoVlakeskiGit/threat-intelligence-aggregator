from datetime import datetime
from pydantic import BaseModel


class LogEntryCreate(BaseModel):
    source_ip: str | None = None
    domain: str | None = None
    event_type: str
    raw_message: str


class LogEntryResponse(BaseModel):
    id: int
    source_ip: str | None = None
    domain: str | None = None
    event_type: str
    raw_message: str
    created_at: datetime

    class Config:
        from_attributes = True