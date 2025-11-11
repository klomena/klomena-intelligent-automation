"""SQLAlchemy model describing Celebration Graph™ edges (v0.1)."""

from sqlalchemy import Column, Float, Integer, String, UniqueConstraint

from ..db import Base


class GraphEdge(Base):
    """
    Represents a directed relationship between two domain nodes.

    Examples:
        - Activity -> AgeGroup (relation_type="SUITABLE_FOR")
        - Theme -> AddOn (relation_type="COMPLEMENTS")
    """

    __tablename__ = "graph_edges"

    id = Column(Integer, primary_key=True, autoincrement=True)
    relation_type = Column(String, nullable=False)

    source_node_type = Column(String, nullable=False)
    source_value = Column(String, nullable=False)
    target_node_type = Column(String, nullable=False)
    target_value = Column(String, nullable=False)

    weight = Column(Float, nullable=False, default=1.0)

    __table_args__ = (
        UniqueConstraint(
            "relation_type",
            "source_node_type",
            "source_value",
            "target_node_type",
            "target_value",
            name="uq_graph_edge",
        ),
    )

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"GraphEdge({self.relation_type}: "
            f"{self.source_node_type}->{self.target_node_type})"
        )
