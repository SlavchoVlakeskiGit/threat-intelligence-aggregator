from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_indicators():
    return {"message": "Indicators endpoint ready for implementation"}