import pytest
from server.app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns correct response"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to my page!' in response.data

def test_user_route_with_string_parameter(client):
    """Test that user route accepts string parameters"""
    response = client.get('/testuser')
    assert response.status_code == 200
    assert b'Profile for testuser' in response.data

def test_user_route_with_different_username(client):
    """Test user route with a different username"""
    response = client.get('/john_doe123')
    assert response.status_code == 200
    assert b'Profile for john_doe123' in response.data

def test_user_route_with_hyphens(client):
    """Test user route with hyphens in username"""
    response = client.get('/user-name-test')
    assert response.status_code == 200
    assert b'Profile for user-name-test' in response.data

def test_user_route_with_numbers(client):
    """Test user route with numbers in username"""
    response = client.get('/user123')
    assert response.status_code == 200
    assert b'Profile for user123' in response.data