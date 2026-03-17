from datetime import datetime
from pydantic import BaseModel


class AlertResponse(BaseModel):
    id: int
    matched_value: str
    indicator_type: str
    severity: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True