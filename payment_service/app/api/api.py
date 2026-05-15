from fastapi import APIRouter, FastAPI


router = APIRouter()
@router.get("/ping")
def ping():
    return {"status": "ok"}