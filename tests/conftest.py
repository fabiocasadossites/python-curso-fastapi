import pytest
from fastapi.testclient import TestClient

from python_fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)  # Setup (Configuração)
