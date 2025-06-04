from mf.pylib import hello


def test_hello():
    assert hello().startswith("Hello from pylib")
