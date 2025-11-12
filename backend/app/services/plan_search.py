"""Plan search service."""
from app.schemas.plan import PlanSearchRequest, PlanSearchResponse


class PlanSearchService:
    """Service for searching celebration plans."""
    
    @staticmethod
    def search(request: PlanSearchRequest) -> PlanSearchResponse:
        """Search for plans based on query."""
        # Minimal implementation - can be enhanced with actual search logic
        plans = [
            {
                "id": "plan_1",
                "name": "Basic Birthday Party",
                "description": "A simple birthday celebration package",
                "city": request.city or "Beirut",
                "estimated_cost": 500.0
            },
            {
                "id": "plan_2",
                "name": "Premium Celebration",
                "description": "An enhanced celebration experience",
                "city": request.city or "Beirut",
                "estimated_cost": 1500.0
            }
        ]
        
        # Filter by city if provided
        if request.city:
            plans = [p for p in plans if p["city"].lower() == request.city.lower()]
        
        # Filter by budget if provided
        if request.budget:
            plans = [p for p in plans if p["estimated_cost"] <= request.budget]
        
        return PlanSearchResponse(
            plans=plans,
            total=len(plans)
        )
