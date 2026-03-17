from sqlalchemy.orm import Session

from app.models.alert import Alert


def create_alert(
    db: Session,
    matched_value: str,
    indicator_type: str,
    severity: str,
    description: str,
) -> Alert:
    alert = Alert(
        matched_value=matched_value,
        indicator_type=indicator_type,
        severity=severity,
        description=description,
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


def list_alerts(db: Session) -> list[Alert]:
    return db.query(Alert).order_by(Alert.id.desc()).all()