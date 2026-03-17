import json
from pathlib import Path
from sqlalchemy.orm import Session

from app.models.indicator import Indicator


def load_feed_data(file_path: str) -> list[dict]:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def import_indicators_from_feed(db: Session, file_path: str) -> dict:
    feed_items = load_feed_data(file_path)
    imported_count = 0
    skipped_count = 0

    for item in feed_items:
        existing_indicator = (
            db.query(Indicator)
            .filter(Indicator.value == item["value"])
            .first()
        )

        if existing_indicator:
            skipped_count += 1
            continue

        indicator = Indicator(
            indicator_type=item["indicator_type"],
            value=item["value"],
            source_name=item["source_name"],
            confidence_score=item["confidence_score"],
        )
        db.add(indicator)
        imported_count += 1

    db.commit()

    return {
        "imported": imported_count,
        "skipped": skipped_count,
        "total": len(feed_items),
    }