"""Schemas for vendor plan search results."""

from typing import List, Literal

from pydantic import BaseModel, Field


class PlanSearchRequest(BaseModel):
    """Structured search parameters coming from the UI or orchestration layer."""

    age: int = Field(..., ge=0, description="Child age in years.")
    area: str = Field(..., min_length=1, description="Preferred area or neighborhood.")
    theme: str = Field(..., min_length=1, description="Desired party theme.")
    budget_tier: Literal["low", "medium", "premium"] = Field(..., description="Budget tier classification.")


class VendorSummary(BaseModel):
    """Minimal vendor info shown to the parent as part of a plan."""

    vendor_id: str = Field(..., description="Unique identifier for the vendor.")
    name: str
    price_band: int = Field(..., ge=1, le=3)
    areas_served: List[str] = Field(default_factory=list)
    services: List[str] = Field(default_factory=list)
    why_matched: List[str] = Field(default_factory=list)


class PlanSearchResponse(BaseModel):
    """List of vendors returned by the plan search."""

    vendors: List[VendorSummary] = Field(default_factory=list)
