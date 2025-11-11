"""Endpoints related to interpreting parent intent."""

from fastapi import APIRouter

from ..schemas.intent import IntentParseRequest, IntentParseResponse
from ..services.intent_parser import parse_intent

router = APIRouter()


@router.post(
    "",
    response_model=IntentParseResponse,
    summary="Parse a parent's celebration request into structured data.",
)
def parse_intent_endpoint(payload: IntentParseRequest) -> IntentParseResponse:
    """
    Use a lightweight heuristic parser to extract the key details we need to
    search for vendors. This is a placeholder for the future LLM integration.
    """

    return parse_intent(payload.message)
