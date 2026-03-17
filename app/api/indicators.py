from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.indicator import Indicator
from app.schemas.indicator import IndicatorCreate, IndicatorResponse
from app.services.feed_service import import_indicators_from_feed

router = APIRouter()


@router.get("/", response_model=list[IndicatorResponse])
def list_indicators(db: Session = Depends(get_db)):
    return db.query(Indicator).order_by(Indicator.id.desc()).all()


@router.post("/", response_model=IndicatorResponse)
def create_indicator(payload: IndicatorCreate, db: Session = Depends(get_db)):
    existing_indicator = (
        db.query(Indicator)
        .filter(Indicator.value == payload.value)
        .first()
    )

    if existing_indicator:
        raise HTTPException(status_code=400, detail="Indicator already exists")

    indicator = Indicator(
        indicator_type=payload.indicator_type,
        value=payload.value,
        source_name=payload.source_name,
        confidence_score=payload.confidence_score,
    )
    db.add(indicator)
    db.commit()
    db.refresh(indicator)
    return indicator


@router.post("/import")
def import_indicators(db: Session = Depends(get_db)):
    result = import_indicators_from_feed(db, "sample_data/threat_feed.json")
    return {
        "message": "Threat feed imported successfully",
        "result": result,
    }