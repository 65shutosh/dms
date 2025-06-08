from fastapi import APIRouter

from app.api.v1.endpoints import auth, deliveries

api_router = APIRouter()

# Import and include other routers here
# Example:
# from app.api.v1.endpoints import users, deliveries, orders
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(deliveries.router, prefix="/deliveries", tags=["deliveries"])
# api_router.include_router(orders.router, prefix="/orders", tags=["orders"])

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(deliveries.router, prefix="/deliveries", tags=["deliveries"]) 