import uuid
from typing import Optional, List
from sqlalchemy.orm import Session

from app.models.delivery import Delivery
from app.schemas.delivery import DeliveryCreate, DeliveryUpdate

def get(db: Session, id: int) -> Optional[Delivery]:
    return db.query(Delivery).filter(Delivery.id == id).first()

def get_by_tracking_number(db: Session, tracking_number: str) -> Optional[Delivery]:
    return db.query(Delivery).filter(Delivery.tracking_number == tracking_number).first()

def get_multi(
    db: Session, *, skip: int = 0, limit: int = 100
) -> List[Delivery]:
    return db.query(Delivery).offset(skip).limit(limit).all()

def get_multi_by_agent(
    db: Session, *, agent_id: int, skip: int = 0, limit: int = 100
) -> List[Delivery]:
    return (
        db.query(Delivery)
        .filter(Delivery.assigned_to == agent_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create(db: Session, *, obj_in: DeliveryCreate) -> Delivery:
    tracking_number = str(uuid.uuid4())[:8].upper()
    db_obj = Delivery(
        tracking_number=tracking_number,
        sender_name=obj_in.sender_name,
        sender_phone=obj_in.sender_phone,
        sender_address=obj_in.sender_address,
        recipient_name=obj_in.recipient_name,
        recipient_phone=obj_in.recipient_phone,
        recipient_address=obj_in.recipient_address,
        package_description=obj_in.package_description,
        weight=obj_in.weight,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(
    db: Session, *, db_obj: Delivery, obj_in: DeliveryUpdate
) -> Delivery:
    update_data = obj_in.dict(exclude_unset=True)
    for field in update_data:
        setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj 