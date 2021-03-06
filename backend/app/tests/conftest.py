from typing import Generator

import pytest
from fastapi.testclient import TestClient
from pydantic import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import Session

from app.config import config
from app.db.base import Base
from app.db.session import engine, SessionLocal
from main import app
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils import get_superuser_token_headers


def setup_db() -> None:
    try:
        conn = engine.connect()
        conn.execute('commit')
        conn.execute(f'drop database {config.TEST_DB}')
        conn.close()
    except ProgrammingError:
        pass

    try:
        conn = engine.connect()
        conn.execute('commit')
        conn.execute(f'create database {config.TEST_DB}')
        conn.close()
    except ProgrammingError:
        pass

    config.SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
        scheme='postgresql',
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_SERVER,
        path=f'/{config.TEST_DB}',
    )
    test_engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(test_engine)
    SessionLocal.configure(bind=test_engine)


@pytest.fixture(scope='session')
def db() -> Generator:
    setup_db()
    yield SessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope='module')
def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope='module')
def normal_user_token_headers(client: TestClient, db: Session) -> dict[str, str]:
    return authentication_token_from_email(
        client=client, email=config.EMAIL_TEST_USER, db=db
    )
