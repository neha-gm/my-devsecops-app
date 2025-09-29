from app import app


def test_hello():
    client = app.test_client()
    response = client.get('/')
    # Bandit flagged assert, but it's safe in pytest tests
    assert response.data == b"Hello from dev!"  # nosec
