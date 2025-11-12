"""Graph repository."""
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.celebration_graph import CelebrationGraph


class GraphRepository:
    """Repository for celebration graph data access."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_edges(
        self,
        source: Optional[str] = None,
        target: Optional[str] = None
    ) -> List[CelebrationGraph]:
        """Get graph edges with optional filters."""
        query = self.db.query(CelebrationGraph)
        
        if source:
            query = query.filter(CelebrationGraph.source == source)
        if target:
            query = query.filter(CelebrationGraph.target == target)
        
        return query.all()
    
    def get_edge_by_id(self, edge_id: int) -> Optional[CelebrationGraph]:
        """Get an edge by ID."""
        return self.db.query(CelebrationGraph).filter(CelebrationGraph.id == edge_id).first()
