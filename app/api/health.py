from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "Threat Intelligence Aggregator",
        "timestamp": datetime.utcnow().isoformat()
    }