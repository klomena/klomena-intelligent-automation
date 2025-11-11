"""Endpoints for recommending add-ons."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..schemas.addon import AddonRecommendationRequest, AddonRecommendationResponse
from ..services.addon_recommender import recommend_addons

router = APIRouter()


@router.post(
    "/recommend",
    response_model=AddonRecommendationResponse,
    summary="Suggest add-ons that fit the celebration brief.",
)
def recommend_addons_endpoint(
    payload: AddonRecommendationRequest,
    db: Session = Depends(get_db),
) -> AddonRecommendationResponse:
    addons = recommend_addons(db, payload)
    return AddonRecommendationResponse(addons=addons)
