from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.log_entry import LogEntryCreate, LogEntryResponse
from app.services.log_service import create_log_entry, import_logs_from_file, list_log_entries

router = APIRouter()


@router.get("/", response_model=list[LogEntryResponse])
def list_logs(db: Session = Depends(get_db)):
    return list_log_entries(db)


@router.post("/", response_model=LogEntryResponse)
def create_log(payload: LogEntryCreate, db: Session = Depends(get_db)):
    return create_log_entry(
        db=db,
        source_ip=payload.source_ip,
        domain=payload.domain,
        event_type=payload.event_type,
        raw_message=payload.raw_message,
    )


@router.post("/import")
def import_logs(db: Session = Depends(get_db)):
    result = import_logs_from_file(db, "sample_data/sample_logs.json")
    return {
        "message": "Sample logs imported successfully",
        "result": result,
    }