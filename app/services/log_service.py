import json
from pathlib import Path

from sqlalchemy.orm import Session

from app.models.log_entry import LogEntry
from app.services.matching_service import check_log_for_matches


def create_log_entry(db: Session, source_ip, domain, event_type: str, raw_message: str) -> LogEntry:
    log_entry = LogEntry(
        source_ip=source_ip,
        domain=domain,
        event_type=event_type,
        raw_message=raw_message,
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)

    check_log_for_matches(db, log_entry)

    return log_entry


def list_log_entries(db: Session) -> list[LogEntry]:
    return db.query(LogEntry).order_by(LogEntry.id.desc()).all()


def import_logs_from_file(db: Session, file_path: str) -> dict:
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        log_items = json.load(file)

    imported_count = 0

    for item in log_items:
        create_log_entry(
            db=db,
            source_ip=item.get("source_ip"),
            domain=item.get("domain"),
            event_type=item["event_type"],
            raw_message=item["raw_message"],
        )
        imported_count += 1

    return {
        "imported": imported_count,
        "total": len(log_items),
    }