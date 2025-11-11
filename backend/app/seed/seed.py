"""
Simple seed script to populate the database with sample vendors and graph edges.

Usage (from the /backend folder):
    poetry run python -m app.seed.seed
"""

from __future__ import annotations

import json
from pathlib import Path

from ..db import SessionLocal
from ..repositories.graph_repository import upsert_graph_edges
from ..repositories.vendor_repository import upsert_vendors

DATA_DIR = Path(__file__).resolve().parent / "data"


def load_json(filename: str) -> list[dict]:
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


def run() -> None:
    """Seed the vendors and graph edges tables with starter data."""

    session = SessionLocal()
    try:
        vendors = load_json("vendors.json")
        edges = load_json("graph_edges.json")

        upsert_vendors(session, vendors)
        upsert_graph_edges(session, edges)

        print(f"Seeded {len(vendors)} vendors and {len(edges)} graph edges.")
    finally:
        session.close()


if __name__ == "__main__":
    run()
