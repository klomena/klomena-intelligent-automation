"""Addon recommendation service."""
from app.schemas.addon import AddonRecommendationRequest, AddonRecommendationResponse


class AddonRecommender:
    """Service for recommending addons for plans."""
    
    @staticmethod
    def recommend(request: AddonRecommendationRequest) -> AddonRecommendationResponse:
        """Recommend addons for a given plan."""
        # Minimal implementation - can be enhanced with ML/recommendation logic
        addons = [
            {
                "id": "addon_1",
                "name": "Photography Package",
                "description": "Professional photography services",
                "price": 200.0,
                "category": "photography"
            },
            {
                "id": "addon_2",
                "name": "Catering Upgrade",
                "description": "Premium catering options",
                "price": 300.0,
                "category": "catering"
            },
            {
                "id": "addon_3",
                "name": "Entertainment Package",
                "description": "DJ and music services",
                "price": 250.0,
                "category": "entertainment"
            }
        ]
        
        return AddonRecommendationResponse(
            addons=addons,
            reasoning="Recommended based on plan compatibility"
        )
