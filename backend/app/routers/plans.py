"""Endpoints that return celebration plans (vendor shortlists)."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..schemas.plan import PlanSearchRequest, PlanSearchResponse
from ..services.plan_search import search_vendors

router = APIRouter()


@router.post(
    "/search",
    response_model=PlanSearchResponse,
    summary="Find top vendors for a celebration brief.",
)
def search_plans(payload: PlanSearchRequest, db: Session = Depends(get_db)) -> PlanSearchResponse:
    vendors = list(search_vendors(db, payload))
    return PlanSearchResponse(vendors=vendors)
