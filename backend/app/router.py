from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils import deps
from .controller import *

router = APIRouter()

@router.post('/upload')
def upload_evidence_endpoint(
  db: Session = Depends(deps.get_db)
) -> Any:
    return upload_evidence(db)
