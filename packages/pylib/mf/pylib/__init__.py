from importlib.metadata import version

__version__ = version('mf-pylib')

def hello() -> str:
    return f"Hello from pylib ({__version__})!"
