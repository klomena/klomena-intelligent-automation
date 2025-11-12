"""Intent parsing router."""
from fastapi import APIRouter
from app.schemas.intent import IntentRequest, IntentResponse
from app.services.intent_parser import IntentParser

router = APIRouter()


@router.post("", response_model=IntentResponse)
async def parse_intent(request: IntentRequest):
    """Parse user intent from text."""
    parser = IntentParser()
    return parser.parse(request)
