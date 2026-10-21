from fastapi.testclient import TestClient
from fastapi_app import app

client = TestClient(app)


def test_read_root():
    """Тест главной страницы FastAPI."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_greet_user():
    """Тест эндпоинта с параметром."""
    response = client.get("/greet/Виктория")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Виктория!"}