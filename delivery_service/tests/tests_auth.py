import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register(client):
    response = client.post('/register', json={
        'nome': 'Teste',
        'email': 'teste@email.com',
        'senha': '123'
    })
    assert response.status_code == 200
    assert b'Cliente registrado com sucesso' in response.data

def test_login_success(client):
    client.post('/register', json={
        'nome': 'Login',
        'email': 'login@email.com',
        'senha': 'abc'
    })
    response = client.post('/login', json={
        'email': 'login@email.com',
        'senha': 'abc'
    })
    assert response.status_code == 200
    assert b'Login bem-sucedido' in response.data

def test_login_fail(client):
    response = client.post('/login', json={
        'email': 'naoexiste@email.com',
        'senha': 'errado'
    })
    assert response.status_code == 401
