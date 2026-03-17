from sqlalchemy.orm import Session

from app.models.indicator import Indicator
from app.models.log_entry import LogEntry
from app.services.alert_service import create_alert


def check_log_for_matches(db: Session, log_entry: LogEntry):
    created_alerts = []

    if log_entry.source_ip:
        matched_ip = (
            db.query(Indicator)
            .filter(
                Indicator.indicator_type == "ip",
                Indicator.value == log_entry.source_ip
            )
            .first()
        )

        if matched_ip:
            alert = create_alert(
                db=db,
                matched_value=log_entry.source_ip,
                indicator_type="ip",
                severity="high",
                description=f"Log entry matched malicious IP indicator: {log_entry.source_ip}",
            )
            created_alerts.append(alert)

    if log_entry.domain:
        matched_domain = (
            db.query(Indicator)
            .filter(
                Indicator.indicator_type == "domain",
                Indicator.value == log_entry.domain
            )
            .first()
        )

        if matched_domain:
            alert = create_alert(
                db=db,
                matched_value=log_entry.domain,
                indicator_type="domain",
                severity="high",
                description=f"Log entry matched malicious domain indicator: {log_entry.domain}",
            )
            created_alerts.append(alert)

    return created_alerts