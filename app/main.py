from fastapi import FastAPI

from app.api import alerts, health, indicators, logs
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend service for threat feed ingestion, log matching, and alert generation."
)

app.include_router(health.router, prefix="/api/health", tags=["Health"])
app.include_router(indicators.router, prefix="/api/indicators", tags=["Indicators"])
app.include_router(logs.router, prefix="/api/logs", tags=["Logs"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alerts"])


@app.get("/")
def root():
    return {
        "message": "Threat Intelligence Aggregator API is running",
        "version": settings.app_version
    }