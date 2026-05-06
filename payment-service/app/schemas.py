from decimal import Decimal
from typing import Optional
from app.models import OrderStatus
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String

Base = declarative_base()

class PaymenCrate(Base):
    __tablename__ = 'Payments'
    id: uuid.UUID
    amount: Decimal
    currency: String
    status: OrderStatus
    description: Optional[str]
    created_at: DateTime
    updated_at: DateTime
    idempotency_key: str
