"""Database seeding script."""
import json
from pathlib import Path
from sqlalchemy.orm import Session
from app.db import Base, engine, SessionLocal
from app.models.vendor import Vendor
from app.models.celebration_graph import CelebrationGraph


def seed_vendors(db: Session):
    """Seed vendors from JSON file."""
    data_path = Path(__file__).parent / "data" / "vendors.json"
    with open(data_path, "r") as f:
        vendors_data = json.load(f)
    
    for vendor_data in vendors_data:
        vendor = Vendor(**vendor_data)
        db.add(vendor)
    
    db.commit()
    print(f"Seeded {len(vendors_data)} vendors")


def seed_graph_edges(db: Session):
    """Seed graph edges from JSON file."""
    data_path = Path(__file__).parent / "data" / "graph_edges.json"
    with open(data_path, "r") as f:
        edges_data = json.load(f)
    
    for edge_data in edges_data:
        edge = CelebrationGraph(**edge_data)
        db.add(edge)
    
    db.commit()
    print(f"Seeded {len(edges_data)} graph edges")


def seed_database():
    """Seed the database with initial data."""
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Check if data already exists
        if db.query(Vendor).count() > 0:
            print("Vendors already seeded, skipping...")
        else:
            seed_vendors(db)
        
        if db.query(CelebrationGraph).count() > 0:
            print("Graph edges already seeded, skipping...")
        else:
            seed_graph_edges(db)
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
