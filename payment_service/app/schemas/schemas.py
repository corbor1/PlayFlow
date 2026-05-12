from decimal import Decimal
from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from app.schemas.schemas import OrderStatus

class PaymentCreate (BaseModel):
    amount: Decimal = Field(... , description="Сумма платежа")
    currency: str = Field(default="RUB", max_length=3, description="Валюта")
    descriptional: Optional[str] = Field(None, max_length=500,description="Описание")
    idempotency_key: str = Field (..., description="Ключ идемпотентности")

class PaymentResponse(PaymentCreate):
    id: uuid.UUID
    status: OrderStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class OutboxEventResponse(BaseModel):
    id: uuid.UUID
    event_type: str
    payload: dict
    create_at: datetime
    publisher: bool

    class Config:
        from_attributes = True