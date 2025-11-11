"""SQLAlchemy model for storing vendor information (Vendor DNA v0.1)."""

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Float, Integer, String, func
from sqlalchemy.dialects.postgresql import ARRAY

from ..db import Base


class Vendor(Base):
    """Represents a celebration vendor in our marketplace."""

    __tablename__ = "vendors"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    areas_served = Column(ARRAY(String), nullable=False)
    categories = Column(ARRAY(String), nullable=False)
    themes = Column(ARRAY(String), nullable=False)

    price_band = Column(Integer, nullable=False)
    age_min = Column(Integer, nullable=False)
    age_max = Column(Integer, nullable=False)

    is_verified = Column(Boolean, nullable=False, default=False)

    response_time_score = Column(Float, nullable=True)
    freshness_score = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint("price_band BETWEEN 1 AND 3", name="price_band_range"),
        CheckConstraint("age_min <= age_max", name="age_range_valid"),
    )

    def __repr__(self) -> str:  # pragma: no cover - for debugging readability
        return f"Vendor(id={self.id!r}, name={self.name!r})"
