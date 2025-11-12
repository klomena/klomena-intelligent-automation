"""Vendor repository."""
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.vendor import Vendor


class VendorRepository:
    """Repository for vendor data access."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_vendors(
        self,
        city: Optional[str] = None,
        category: Optional[str] = None
    ) -> List[Vendor]:
        """Get vendors with optional filters."""
        query = self.db.query(Vendor)
        
        if city:
            query = query.filter(Vendor.city == city)
        if category:
            query = query.filter(Vendor.category == category)
        
        return query.all()
    
    def get_vendor_by_id(self, vendor_id: int) -> Optional[Vendor]:
        """Get a vendor by ID."""
        return self.db.query(Vendor).filter(Vendor.id == vendor_id).first()
