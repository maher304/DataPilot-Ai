import pytest
from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["read_only_enforced"] == True

def test_schema():
    response = client.get("/schema")
    assert response.status_code == 200
    data = response.json()
    assert "tables" in data

def test_query_revenue():
    response = client.post("/query", json={"question": "Which product categories generated the highest revenue?"})
    assert response.status_code == 200
    data = response.json()
    assert "sql" in data
    assert "answer" in data
    assert data["validated"] == True
    assert data["execution_metadata"]["read_only"] == True
