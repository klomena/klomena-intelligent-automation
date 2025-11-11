"""Schemas for add-on recommendations."""

from typing import List, Literal

from pydantic import BaseModel, Field


class AddonRecommendationRequest(BaseModel):
    """Parameters used to look up celebration add-ons."""

    age: int = Field(..., ge=0, description="Child age in years.")
    theme: str = Field(..., min_length=1, description="Selected celebration theme.")
    budget_tier: Literal["low", "medium", "premium"] = Field(..., description="Budget tier classification.")


class AddonSuggestion(BaseModel):
    """Single add-on suggestion returned to the parent."""

    name: str = Field(..., description="Human-readable add-on name.")
    reason: str = Field(..., description="Friendly explanation of why we are recommending it.")


class AddonRecommendationResponse(BaseModel):
    """Collection of add-on suggestions."""

    addons: List[AddonSuggestion] = Field(default_factory=list)
