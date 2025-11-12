"""Celebration graph model."""
from sqlalchemy import Column, Integer, String, JSON
from app.db import Base


class CelebrationGraph(Base):
    """Celebration graph edge model."""
    
    __tablename__ = "celebration_graph_edges"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False, index=True)
    target = Column(String, nullable=False, index=True)
    relationship_type = Column(String)  # e.g., "requires", "enhances", "suggests"
    weight = Column(Integer, default=1)  # Edge weight for graph algorithms
    metadata = Column(JSON)  # Additional edge information
