# tests/test_api.py
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the SQL Query Chatbot API"}


def test_query_post():
    response = client.post("/query/", json={"user_input": "select users with age over 30"})
    assert response.status_code == 200
    assert "sql_query" in response.json()
    assert "results" in response.json()


def test_invalid_query():
    response = client.post("/query/", json={"user_input": "invalid query"})
    assert response.status_code == 200
