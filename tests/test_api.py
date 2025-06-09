import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_query_post():
    """Test valid query processing."""
    response = client.post(
        "/query/", json={"query": "SELECT * FROM users WHERE department = 'research'"}
    )
    assert response.status_code == 200
    assert "result" in response.json()


def test_invalid_query():
    """Test handling of invalid query."""
    response = client.post("/query/", json={"query": "invalid query"})
    assert response.status_code == 200
    assert "error" in response.json()
    assert "Invalid query provided" in response.json()["error"]
