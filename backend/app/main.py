"""Main FastAPI application."""
from fastapi import FastAPI

from app.config import settings
from app.routers import intent, plans, addons, vendors

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

# Healthcheck endpoint
@app.get("/health")
async def healthcheck():
    """Health check endpoint."""
    return {"status": "healthy"}

# Mount routers
app.include_router(intent.router, prefix="/parse-intent", tags=["intent"])
app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(addons.router, prefix="/addons", tags=["addons"])
app.include_router(vendors.router, prefix="/vendors", tags=["vendors"])
