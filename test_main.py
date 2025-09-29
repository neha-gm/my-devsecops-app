from main import greet


def test_greet():
    # Bandit flagged assert, but it's safe in pytest tests
    assert greet("Neha") == "Hello, Neha!"  # nosec
