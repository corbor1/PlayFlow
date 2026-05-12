from fastapi import APIRouter, FastAPI
from schemas import PaymentCreate, PaymentResponse

router = APIRouter()
@router.post("/register")
def create_transaction():
    return {"message": "User registered successfully!"}