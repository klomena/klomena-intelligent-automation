"""Route registration for the FastAPI application."""

from fastapi import APIRouter

from .addons import router as addons_router
from .intent import router as intent_router
from .plans import router as plans_router
from .vendors import router as vendors_router

api_router = APIRouter()
api_router.include_router(intent_router, prefix="/parse-intent", tags=["intent"])
api_router.include_router(plans_router, prefix="/plans", tags=["plans"])
api_router.include_router(addons_router, prefix="/addons", tags=["addons"])
api_router.include_router(vendors_router, prefix="/vendors", tags=["vendors"])
