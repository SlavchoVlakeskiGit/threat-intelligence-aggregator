from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_alerts_endpoint():
    response = client.get("/api/alerts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
