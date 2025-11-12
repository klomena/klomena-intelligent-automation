"""Addon recommendation schemas."""
from pydantic import BaseModel
from typing import List, Optional


class AddonRecommendationRequest(BaseModel):
    """Request schema for addon recommendations."""
    plan_id: str
    context: Optional[dict] = None


class AddonRecommendationResponse(BaseModel):
    """Response schema for addon recommendations."""
    addons: List[dict]
    reasoning: Optional[str] = None
