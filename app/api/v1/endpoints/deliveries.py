from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.delivery import Delivery, DeliveryCreate, DeliveryUpdate, DeliveryWithAgent
from app.services import delivery_service
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Delivery)
def create_delivery(
    *,
    db: Session = Depends(deps.get_db),
    delivery_in: DeliveryCreate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new delivery.
    """
    delivery = delivery_service.create(db, obj_in=delivery_in)
    return delivery

@router.get("/", response_model=List[DeliveryWithAgent])
def read_deliveries(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve deliveries.
    """
    if current_user.is_superuser:
        deliveries = delivery_service.get_multi(db, skip=skip, limit=limit)
    else:
        deliveries = delivery_service.get_multi_by_agent(
            db, agent_id=current_user.id, skip=skip, limit=limit
        )
    return deliveries

@router.get("/{delivery_id}", response_model=DeliveryWithAgent)
def read_delivery(
    *,
    db: Session = Depends(deps.get_db),
    delivery_id: int,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Get delivery by ID.
    """
    delivery = delivery_service.get(db, id=delivery_id)
    if not delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found",
        )
    if not current_user.is_superuser and delivery.assigned_to != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    return delivery

@router.put("/{delivery_id}", response_model=Delivery)
def update_delivery(
    *,
    db: Session = Depends(deps.get_db),
    delivery_id: int,
    delivery_in: DeliveryUpdate,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Update a delivery.
    """
    delivery = delivery_service.get(db, id=delivery_id)
    if not delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found",
        )
    if not current_user.is_superuser and delivery.assigned_to != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    delivery = delivery_service.update(db, db_obj=delivery, obj_in=delivery_in)
    return delivery

@router.get("/track/{tracking_number}", response_model=Delivery)
def track_delivery(
    *,
    db: Session = Depends(deps.get_db),
    tracking_number: str,
) -> Any:
    """
    Track delivery by tracking number.
    """
    delivery = delivery_service.get_by_tracking_number(db, tracking_number=tracking_number)
    if not delivery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delivery not found",
        )
    return delivery 