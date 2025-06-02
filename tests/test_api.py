import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.post("/ask", json={"question": "Who is the CEO of Google?"})
    assert response.status_code == 200
    assert "Sundar Pichai" in response.json()["answer"]
