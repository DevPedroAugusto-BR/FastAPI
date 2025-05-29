import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from learning_fastapi.app import app
from learning_fastapi.models import table_registry


@pytest.fixture
def client():
    def get_session_override():
        return session 
    
    with TestClient(app) as client:
        app.dependency_overrides[get_session_override] = get_session_override
        yield client

    app.dependency_overrides.clear()

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)

from contextlib import contextmanager
from datetime import datetime

# ...
from sqlalchemy import create_engine, event
# ...

@contextmanager 
def _mock_db_time(*, model, time=datetime(2024, 1, 1)): 

    def fake_time_hook(mapper, connection, target): 
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook) 

    yield time 

    event.remove(model, 'before_insert', fake_time_hook)

from dataclasses import asdict

from sqlalchemy import select

from learning_fastapi.models import User

@pytest.fixture
def mock_db_time():
    return _mock_db_time