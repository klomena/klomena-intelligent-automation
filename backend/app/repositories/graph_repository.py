"""Helper functions for the Celebration Graph edges table."""

from __future__ import annotations

from collections.abc import Iterable

from sqlalchemy.orm import Session

from ..models import GraphEdge


def list_graph_edges(db: Session, relation_type: str | None = None) -> list[GraphEdge]:
    """Return graph edges, optionally filtered by relation type."""

    query = db.query(GraphEdge)
    if relation_type:
        query = query.filter(GraphEdge.relation_type == relation_type)
    return query.all()


def upsert_graph_edges(db: Session, edge_payloads: Iterable[dict]) -> None:
    """
    Insert or update edges from a payload.

    We rely on the unique constraint defined on the model so duplicates are
    collapsed automatically when `merge` runs.
    """

    for payload in edge_payloads:
        db.merge(GraphEdge(**payload))
    db.commit()
