from datetime import datetime
from pydantic import BaseModel


class IndicatorCreate(BaseModel):
    indicator_type: str
    value: str
    source_name: str
    confidence_score: int = 50


class IndicatorResponse(BaseModel):
    id: int
    indicator_type: str
    value: str
    source_name: str
    confidence_score: int
    created_at: datetime

    class Config:
        from_attributes = True