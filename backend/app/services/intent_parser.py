"""Simple heuristic intent parsing before the LLM integration lands."""

import re
from typing import Iterable

from ..schemas.intent import IntentParseResponse

# A very small list to keep v0.1 simple. We can expand (or load from DB) later.
KNOWN_THEMES = {
    "unicorn": "Unicorn",
    "mermaid": "Mermaid",
    "space": "Space",
    "football": "Football",
    "princess": "Princess",
}

KNOWN_AREAS = {
    "dbaye": "Dbaye",
    "beirut": "Beirut",
    "jounieh": "Jounieh",
}


def _find_first_keyword(message: str, keywords: Iterable[str]) -> str | None:
    lowered = message.lower()
    for keyword in keywords:
        if keyword in lowered:
            return keyword
    return None


def _detect_budget_tier(amount: float | None) -> str:
    if amount is None:
        return "unknown"
    if amount <= 200:
        return "low"
    if amount <= 600:
        return "medium"
    return "premium"


def parse_intent(message: str) -> IntentParseResponse:
    """
    Extract age, area, theme, and budget details from a free-form message.

    The goal is not perfect accuracy yet; we want predictable and explainable
    behavior for the pilot. When we integrate an LLM we can replace this file.
    """

    age_match = re.search(r"(\d{1,2})\s*(?:year|yr|yo)", message, re.IGNORECASE)
    age = int(age_match.group(1)) if age_match else None

    budget_match = re.search(r"\$?\s*(\d{2,5})(?:\s*(?:usd|dollars))?", message, re.IGNORECASE)
    budget_amount = float(budget_match.group(1)) if budget_match else None
    budget_tier = _detect_budget_tier(budget_amount)

    theme_keyword = _find_first_keyword(message, KNOWN_THEMES.keys())
    theme = KNOWN_THEMES.get(theme_keyword, None)

    area_keyword = _find_first_keyword(message, KNOWN_AREAS.keys())
    area = KNOWN_AREAS.get(area_keyword, None)

    return IntentParseResponse(
        age=age,
        area=area,
        theme=theme,
        budget_amount=budget_amount,
        budget_tier=budget_tier,
    )
