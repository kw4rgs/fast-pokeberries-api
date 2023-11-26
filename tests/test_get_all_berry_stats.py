import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

# Test for successful response
def test_get_all_berry_stats(client):
    response = client.get("api/v1/allBerryStats")
    assert response.status_code == 200
    assert response.json().get('error') == False
    
# Test for Not Found response
def test_get_all_berry_stats_not_found(client):
    response = client.get("/allBerryStats")
    assert response.status_code == 404
    assert response.json().get('detail') == "Not Found"
    
#Test for Internal Server Error response
def test_get_all_berry_stats_internal_server_error(client, monkeypatch):
    monkeypatch.delenv('POKEBERRIES_API_URL', raising=False)
    response = client.get("api/v1/allBerryStats")
    assert response.status_code == 500

# Test for Method Not Allowed response
def test_get_all_berry_stats_method_not_allowed(client):
    response = client.post("/api/v1/allBerryStats")
    assert response.status_code == 405
    assert response.json().get('detail') == "Method Not Allowed"
    
# Test when the environment variable is missing
def test_error_handling_missing_url(client, monkeypatch):
    monkeypatch.delenv('POKEBERRIES_API_URL', raising=False)
    response = client.get("/api/v1/allBerryStats")
    assert response.status_code == 500
    assert response.json().get('detail') == "Missing API URL"
    
# Test for specific keys in the response
def test_get_all_items(client):
    response = client.get("/api/v1/allBerryStats")
    assert response.status_code == 200
    assert response.json().get('error') == False
    assert 'data' in response.json() 
    data = response.json()['data']

    assert 'berries_names' in data
    assert 'min_growth_time' in data
    assert 'median_growth_time' in data
    assert 'max_growth_time' in data
    assert 'variance_growth_time' in data
    assert 'mean_growth_time' in data
    assert 'frequency_growth_time' in data


