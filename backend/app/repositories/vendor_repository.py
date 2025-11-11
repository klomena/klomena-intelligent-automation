"""Utility functions for interacting with the `vendors` table."""

from __future__ import annotations

from collections.abc import Iterable
from typing import List

from sqlalchemy.orm import Session

from ..models import Vendor


def list_vendors(db: Session) -> List[Vendor]:
    """Return all vendors. In v0.1 we keep this simple without pagination."""

    return db.query(Vendor).order_by(Vendor.name.asc()).all()


def upsert_vendors(db: Session, vendor_payloads: Iterable[dict]) -> None:
    """
    Insert or update vendors from a payload (used by the seed script).

    For small data volumes a `Session.merge` is easy to understand. Later we can
    optimize with `ON CONFLICT` or bulk operations.
    """

    for payload in vendor_payloads:
        db.merge(Vendor(**payload))
    db.commit()
