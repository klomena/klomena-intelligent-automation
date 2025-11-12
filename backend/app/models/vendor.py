"""Vendor model."""
from sqlalchemy import Column, Integer, String, Float, JSON
from app.db import Base


class Vendor(Base):
    """Vendor database model."""
    
    __tablename__ = "vendors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    city = Column(String, nullable=False, index=True)
    category = Column(String, nullable=False)
    price_range = Column(String)  # e.g., "low", "medium", "high"
    rating = Column(Float)
    metadata = Column(JSON)  # Additional vendor information
