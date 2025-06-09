from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_query_post():
    """Test valid query processing."""
    response = client.post(
        "/query/", json={"query": "select users with from research department"}
    )
    assert response.status_code == 200


def test_invalid_query():
    """Test handling of invalid query."""
    response = client.post("/query/", json={"query": "invalid query"})
    assert response.status_code == 200  # Or change to 400 if you handle it differently
