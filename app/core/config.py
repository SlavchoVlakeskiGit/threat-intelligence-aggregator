import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name: str = os.getenv("APP_NAME", "Threat Intelligence Aggregator")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://threat_user:threatpass123@127.0.0.1:3306/threat_intel_db"
    )


settings = Settings()