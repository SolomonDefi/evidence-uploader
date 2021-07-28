from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Session

from app.db.base_class import Base
from app.db.crud import CRUDBase
from app.schemas.upload_item import UploadItemCreate, UploadItemUpdate

class UploadItem(Base):
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='items')


class CRUDItem(CRUDBase[UploadItem, UploadItemCreate, UploadItemUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: UploadItemCreate, owner_id: int
    ) -> UploadItem:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[UploadItem]:
        return (
            db.query(self.model)
            .filter(UploadItem.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


item = CRUDItem(UploadItem)
