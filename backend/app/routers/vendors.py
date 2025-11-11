"""Endpoints for basic vendor administration/debugging."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..repositories.vendor_repository import list_vendors
from ..schemas.plan import VendorSummary

router = APIRouter()


@router.get(
    "",
    response_model=list[VendorSummary],
    summary="List all vendors currently stored in the database.",
)
def list_all_vendors(db: Session = Depends(get_db)) -> list[VendorSummary]:
    vendors = list_vendors(db)
    return [
        VendorSummary(
            vendor_id=vendor.id,
            name=vendor.name,
            price_band=vendor.price_band,
            areas_served=vendor.areas_served,
            services=vendor.categories,
            why_matched=[],
        )
        for vendor in vendors
    ]
