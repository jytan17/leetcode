import sys
from pathlib import Path


def pytest_collectstart(collector):
    path = Path(str(collector.fspath))
    if path.is_dir():
        return
    problem_dir = path.parent
    if not (problem_dir / "solution.py").exists():
        return
    sys.modules.pop("solution", None)
    p = str(problem_dir)
    while p in sys.path:
        sys.path.remove(p)
    sys.path.insert(0, p)
