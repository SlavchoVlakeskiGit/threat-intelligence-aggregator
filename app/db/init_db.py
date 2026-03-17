from app.db.database import Base, engine
from app.models.alert import Alert
from app.models.indicator import Indicator
from app.models.log_entry import LogEntry


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")