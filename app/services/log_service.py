from sqlalchemy.orm import Session

from app.models.log_entry import LogEntry


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
    return log_entry


def list_log_entries(db: Session) -> list[LogEntry]:
    return db.query(LogEntry).order_by(LogEntry.id.desc()).all()