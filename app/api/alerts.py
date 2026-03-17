from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_alerts():
    return {"message": "Alerts endpoint ready for implementation"}