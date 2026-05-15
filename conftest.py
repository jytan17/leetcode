import sys
from pathlib import Path


def pytest_collectstart(collector):
    path = Path(str(collector.fspath))
    for parent in path.parents:
        if parent.name == "python" and parent.parent.parent.name == "problems":
            p = str(parent)
            if p not in sys.path:
                sys.path.insert(0, p)
            break
