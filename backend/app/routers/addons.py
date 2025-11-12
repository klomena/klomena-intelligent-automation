"""Addon recommendation router."""
from fastapi import APIRouter
from app.schemas.addon import AddonRecommendationRequest, AddonRecommendationResponse
from app.services.addon_recommender import AddonRecommender

router = APIRouter()


@router.post("/recommend", response_model=AddonRecommendationResponse)
async def recommend_addons(request: AddonRecommendationRequest):
    """Recommend addons for a plan."""
    recommender = AddonRecommender()
    return recommender.recommend(request)
