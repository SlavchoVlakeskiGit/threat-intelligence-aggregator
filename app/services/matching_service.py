from sqlalchemy.orm import Session

from app.models.indicator import Indicator
from app.models.log_entry import LogEntry
from app.services.alert_service import create_alert


def get_severity_from_confidence(confidence_score: int) -> str:
    if confidence_score >= 85:
        return "high"
    if confidence_score >= 60:
        return "medium"
    return "low"


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
                severity=get_severity_from_confidence(matched_ip.confidence_score),
                description=(
                    f"Log entry matched malicious IP indicator: {log_entry.source_ip} "
                    f"(confidence: {matched_ip.confidence_score})"
                ),
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
                severity=get_severity_from_confidence(matched_domain.confidence_score),
                description=(
                    f"Log entry matched malicious domain indicator: {log_entry.domain} "
                    f"(confidence: {matched_domain.confidence_score})"
                ),
            )
            created_alerts.append(alert)

    return created_alerts