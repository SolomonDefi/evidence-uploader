from sqlalchemy.orm import Session

from app import models, schemas
from app.config import config
from app.db import base  # noqa: F401

# Import all SQLAlchemy models (app.db.base) before initializing DB

def init_db(db: Session) -> None:
    # Tables created with Alembic migrations

    admin_email = config.INITIAL_ADMIN_EMAIL
    user = models.CRUDUser.get_by_email(db, email=admin_email)
    if not user:
        user_in = schemas.UserCreate(
            email=admin_email,
            password=config.INITIAL_ADMIN_PASSWORD,
            is_superuser=True,
        )
        user = models.CRUDUser.create(db, obj_in=user_in)  # noqa: F841
