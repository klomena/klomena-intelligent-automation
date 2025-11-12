"""Plan search router."""
from fastapi import APIRouter
from app.schemas.plan import PlanSearchRequest, PlanSearchResponse
from app.services.plan_search import PlanSearchService

router = APIRouter()


@router.post("/search", response_model=PlanSearchResponse)
async def search_plans(request: PlanSearchRequest):
    """Search for celebration plans."""
    service = PlanSearchService()
    return service.search(request)
