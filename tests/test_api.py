from fastapi.testclient import TestClient

from pydantic import BaseModel
from app.main import app

client = TestClient(app)


class QueryInput(BaseModel):
    user_input: str


def test_root():
    """Test the root endpoint returns the welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the SQL Query Chatbot API"}


def test_query_post():
    """Test valid query processing."""
    response = client.post(
        "/query/", json={"user_input": "select users with from research department"}
    )
    assert response.status_code == 200
    assert "sql_query" in response.json()
    assert "results" in response.json()


def test_invalid_query():
    """Test handling of invalid query."""
    response = client.post("/query/", json={"user_input": "invalid query"})
    assert response.status_code == 200
