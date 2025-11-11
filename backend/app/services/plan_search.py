"""Vendor search logic that powers `/plans/search`."""

from __future__ import annotations

from collections.abc import Sequence

from sqlalchemy.orm import Session

from ..models import Vendor
from ..schemas.plan import PlanSearchRequest, VendorSummary

BUDGET_TIER_TO_BAND = {"low": 1, "medium": 2, "premium": 3}


def _score_vendor(vendor: Vendor, request: PlanSearchRequest) -> tuple[float, list[str]]:
    score = 0.0
    reasons: list[str] = []

    if request.area.lower() in (area.lower() for area in vendor.areas_served):
        score += 2.0
        reasons.append(f"Serves {request.area}")

    if request.theme.lower() in (theme.lower() for theme in vendor.themes):
        score += 2.0
        reasons.append(f"Experienced with {request.theme} theme")

    if vendor.age_min <= request.age <= vendor.age_max:
        score += 1.5
        reasons.append("Fits the age range for your child")

    desired_band = BUDGET_TIER_TO_BAND.get(request.budget_tier)
    if desired_band:
        if vendor.price_band == desired_band:
            score += 1.5
            reasons.append("Pricing aligns with your budget tier")
        else:
            # small penalty for being off
            score -= abs(vendor.price_band - desired_band) * 0.5

    if vendor.is_verified:
        score += 0.5
        reasons.append("Vendor is verified by Klomena")

    return score, reasons


def search_vendors(db: Session, request: PlanSearchRequest, limit: int = 6) -> Sequence[VendorSummary]:
    """
    Fetch vendors from the database, apply lightweight filtering + scoring,
    and return a ranked shortlist suitable for the MVP.
    """

    vendors = db.query(Vendor).all()

    shortlisted: list[tuple[Vendor, float, list[str]]] = []
    for vendor in vendors:
        if request.area and request.area.lower() not in (area.lower() for area in vendor.areas_served):
            # Allow near-by vendors: skip hard rejection, but lower score below 0 later.
            pass

        if request.theme and request.theme.lower() not in (theme.lower() for theme in vendor.themes):
            continue

        if request.age < vendor.age_min or request.age > vendor.age_max:
            continue

        score, reasons = _score_vendor(vendor, request)
        if score <= 0:
            continue
        shortlisted.append((vendor, score, reasons))

    shortlisted.sort(key=lambda item: item[1], reverse=True)
    top_vendors = shortlisted[:limit]

    return [
        VendorSummary(
            vendor_id=vendor.id,
            name=vendor.name,
            price_band=vendor.price_band,
            areas_served=vendor.areas_served,
            services=vendor.categories,
            why_matched=reasons,
        )
        for vendor, _score, reasons in top_vendors
    ]
