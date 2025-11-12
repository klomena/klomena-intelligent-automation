"""Intent parsing schemas."""
from pydantic import BaseModel
from typing import Optional, List


class IntentRequest(BaseModel):
    """Request schema for intent parsing."""
    text: str


class IntentResponse(BaseModel):
    """Response schema for intent parsing."""
    intent: str
    entities: Optional[List[dict]] = None
    confidence: float
