import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_data(client):
    response = client.get("/api/data")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_data_by_type(client):
    # Test one known file type, e.g., csv
    response = client.get("/api/data/csv")
    assert response.status_code == 200
    data = response.get_json()
    # The returned data should be a list; if non-empty, each record should be from csv
    assert isinstance(data, list)
    if data:
        assert data[0].get("file_type") == "csv"