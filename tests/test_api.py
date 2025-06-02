from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_query_salary_above():
    response = client.post(""/query/"", json={"user_input"": ""Show employees with salary above 60000""})
    assert response.status_code == 200
    assert ""sql_query"" in response.json()
    assert ""results"" in response.json()
    assert len(response.json()[""results""]) > 10000  # Expect many results with 50,000 records


def test_query_department():
    response = client.post(""/query/"", json={"user_input"": ""Show employees in IT department""})
    assert response.status_code == 200
    assert ""sql_query"" in response.json()
    assert ""results"" in response.json()
    assert len(response.json()[""results""]) > 5000  # Expect several thousand IT employees
    assert all(""IT"" in result[""department""] for result in response.json()[""results""])
