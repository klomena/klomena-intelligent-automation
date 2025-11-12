"""Plan search schemas."""
from pydantic import BaseModel
from typing import Optional, List


class PlanSearchRequest(BaseModel):
    """Request schema for plan search."""
    query: str
    city: Optional[str] = None
    budget: Optional[float] = None


class PlanSearchResponse(BaseModel):
    """Response schema for plan search."""
    plans: List[dict]
    total: int
