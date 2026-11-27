from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_liveness():
    response = client.get('/api/v1/health/live')
    assert response.status_code == 200
    assert response.json() == {'status': 'alive'}


def test_readiness_fails_closed():
    response = client.get('/api/v1/health/ready')
    assert response.status_code == 503
    assert response.json() == {'status': 'not_ready'}


def test_no_secret_or_runtime_details():
    for path in ('live', 'ready'):
        assert set(client.get(f'/api/v1/health/{path}').json()) == {'status'}


def test_openapi_contract():
    paths = app.openapi()['paths']
    assert '200' in paths['/api/v1/health/live']['get']['responses']
    assert '503' in paths['/api/v1/health/ready']['get']['responses']
