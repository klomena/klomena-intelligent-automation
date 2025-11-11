"""Add-on recommendation logic backed by the Celebration Graph™."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from sqlalchemy.orm import Session

from ..models import GraphEdge
from ..schemas.addon import AddonRecommendationRequest, AddonSuggestion

AGE_GROUP_LABELS = {
    range(1, 3): "AgeGroup:1-2",
    range(3, 6): "AgeGroup:3-5",
    range(6, 9): "AgeGroup:6-8",
    range(9, 13): "AgeGroup:9-12",
}


def _age_to_node(age: int) -> str | None:
    for age_range, label in AGE_GROUP_LABELS.items():
        if age in age_range:
            return label
    return None


def recommend_addons(
    db: Session,
    request: AddonRecommendationRequest,
    limit: int = 4,
) -> List[AddonSuggestion]:
    """
    Score and rank add-ons based on Celebration Graph edges.

    We combine signals:
        - Theme complements (Theme -> AddOn edges)
        - Age suitability (AgeGroup <-> AddOn edges)
    """

    scores: Dict[str, float] = defaultdict(float)
    reasons: Dict[str, List[str]] = defaultdict(list)

    # Theme complements
    theme_edges = (
        db.query(GraphEdge)
        .filter(
            GraphEdge.relation_type == "COMPLEMENTS",
            GraphEdge.source_node_type == "Theme",
            GraphEdge.source_value.ilike(f"%{request.theme}%"),
        )
        .all()
    )
    for edge in theme_edges:
        scores[edge.target_value] += edge.weight * 1.5
        reasons[edge.target_value].append(f"Pairs nicely with the {request.theme} theme")

    # Age suitability
    age_node = _age_to_node(request.age)
    if age_node:
        age_edges = (
            db.query(GraphEdge)
            .filter(
                GraphEdge.relation_type == "SUITABLE_FOR",
                GraphEdge.target_node_type == "AgeGroup",
                GraphEdge.target_value == age_node,
            )
            .all()
        )
        for edge in age_edges:
            scores[edge.source_value] += edge.weight
            reasons[edge.source_value].append("Popular for this age group")

    # Lightweight budget adjustment: penalize premium add-ons for low budgets.
    if request.budget_tier == "low":
        for addon in list(scores.keys()):
            scores[addon] *= 0.8
            reasons[addon].append("Budget friendly option")
    elif request.budget_tier == "premium":
        for addon in list(scores.keys()):
            scores[addon] *= 1.1

    ranked_addons = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:limit]

    suggestions = [
        AddonSuggestion(name=name, reason=", ".join(reasons[name]))
        for name, score in ranked_addons
        if score > 0
    ]

    return suggestions
