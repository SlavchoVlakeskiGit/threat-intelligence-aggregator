from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.alert import AlertResponse
from app.services.alert_service import list_alerts

router = APIRouter()


@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return list_alerts(db)