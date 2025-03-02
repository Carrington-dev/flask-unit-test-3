from src import app
from pytest import fixture

@fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hi Carrington, my name is Wonderful'}