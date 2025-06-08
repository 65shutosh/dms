from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.delivery import DeliveryStatus

class DeliveryBase(BaseModel):
    sender_name: str
    sender_phone: str
    sender_address: str
    recipient_name: str
    recipient_phone: str
    recipient_address: str
    package_description: Optional[str] = None
    weight: Optional[float] = None

class DeliveryCreate(DeliveryBase):
    pass

class DeliveryUpdate(BaseModel):
    status: Optional[DeliveryStatus] = None
    assigned_to: Optional[int] = None

class DeliveryInDBBase(DeliveryBase):
    id: int
    tracking_number: str
    status: DeliveryStatus
    assigned_to: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Delivery(DeliveryInDBBase):
    pass

class DeliveryWithAgent(Delivery):
    delivery_agent: Optional[dict] = None 