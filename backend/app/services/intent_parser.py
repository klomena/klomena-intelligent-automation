"""Intent parsing service."""
from app.schemas.intent import IntentRequest, IntentResponse


class IntentParser:
    """Service for parsing user intent from text."""
    
    @staticmethod
    def parse(request: IntentRequest) -> IntentResponse:
        """Parse intent from user text."""
        # Minimal implementation - can be enhanced with NLP
        text_lower = request.text.lower()
        
        # Simple keyword-based intent detection
        if any(word in text_lower for word in ["birthday", "party", "celebration"]):
            intent = "plan_celebration"
        elif any(word in text_lower for word in ["vendor", "supplier", "service"]):
            intent = "find_vendor"
        elif any(word in text_lower for word in ["addon", "add-on", "extra"]):
            intent = "recommend_addon"
        else:
            intent = "general_query"
        
        return IntentResponse(
            intent=intent,
            entities=[],
            confidence=0.7
        )
