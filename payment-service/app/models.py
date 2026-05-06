from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, String, Boolean, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
import uuid

from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
import uuid
import enum
from enum import Enum

from sqlalchemy import Column
Base = BaseModel

class OrderStatus(enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Payments(Base):
    __tablename__ = "Payments"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable= False)
    currency:  Mapped[str] = mapped_column(String(3), nullable=False, default= "RUB")
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus),nullable=False, default=OrderStatus.PENDING)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), nullable= False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    idempotency_key: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)


class Outbox_events(Base):
    __tablename__ = "Outbox_events"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type: Mapped[str] = mapped_column(String(255), nullable=False)
    payload: Mapped[dict] = mapped_column (JSON, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), nullable= False)
    published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)