"""Schemas for parsing user intent."""

from typing import Literal

from pydantic import BaseModel, Field


class IntentParseRequest(BaseModel):
    """Incoming free-text message from a parent."""

    message: str = Field(..., example="I want a unicorn party for my 6 year old in Dbaye with $300 budget")


class IntentParseResponse(BaseModel):
    """Structured fields extracted from the free-text message."""

    age: int | None = Field(None, description="Child age in years, if detected.")
    area: str | None = Field(None, description="Target area or neighborhood.")
    theme: str | None = Field(None, description="Party theme, normalized if possible.")
    budget_amount: float | None = Field(None, description="Exact budget amount in USD if mentioned.")
    budget_tier: Literal["low", "medium", "premium", "unknown"] = "unknown"
