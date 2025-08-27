from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_consulta_valida():
    response = client.get("/api/v1/personas/12345678")
    assert response.status_code == 200

def test_cedula_invalida():
    response = client.get("/api/v1/personas/ABC-001")
    assert response.status_code == 400

def test_cedula_no_encontrada():
    response = client.get("/api/v1/personas/00000000")
    assert response.status_code == 404