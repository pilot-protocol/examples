"""Smoke tests for the Python SDK example scripts.

Goals
-----
Catch regressions in the user-facing demos as the Pilot Protocol Python
SDK evolves. The demos themselves require a live daemon and trusted
peers to execute, so we cannot import them and run them under pytest.
Instead, we validate two cheap properties per demo:

1. The file is syntactically valid Python (``ast.parse``).
2. The demo gates its side-effect entry point on
   ``if __name__ == "__main__":`` so that future ``importlib``-based
   loaders can introspect it without firing real network calls.

Adding a new demo? Drop it next to ``basic_usage.py`` and it is picked
up automatically by ``iter_demo_files``.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest


EXAMPLES_DIR = Path(__file__).resolve().parent.parent


def iter_demo_files() -> list[Path]:
    """Return every top-level ``*.py`` file in ``python_sdk/``.

    Tests under ``python_sdk/tests/`` are intentionally excluded so the
    suite never tries to syntax-check itself.
    """
    return sorted(p for p in EXAMPLES_DIR.glob("*.py") if p.is_file())


DEMOS = iter_demo_files()


def test_demo_directory_is_non_empty() -> None:
    """Guard against the glob silently matching zero files.

    Without this, a future refactor that moves the demos to a sub-package
    would turn every parameterized test below into a no-op and the suite
    would still pass green.
    """
    assert DEMOS, f"no demos found in {EXAMPLES_DIR}"


@pytest.mark.parametrize("demo", DEMOS, ids=lambda p: p.name)
def test_demo_parses_as_valid_python(demo: Path) -> None:
    """The demo must be syntactically valid Python.

    ``ast.parse`` is a pure parse — no imports run, so a missing SDK
    install does not cause spurious failures. This catches accidental
    syntax breakage from search-and-replace edits across the demos.
    """
    source = demo.read_text(encoding="utf-8")
    try:
        ast.parse(source, filename=str(demo))
    except SyntaxError as e:  # pragma: no cover - failure path
        pytest.fail(f"{demo.name} failed to parse: {e}")


@pytest.mark.parametrize("demo", DEMOS, ids=lambda p: p.name)
def test_demo_guards_entry_point(demo: Path) -> None:
    """The demo must gate side effects on ``if __name__ == "__main__"``.

    Importing a demo (via ``importlib`` or ``python -c "import foo"``)
    should never connect to a daemon, open sockets, or block on input.
    Without the guard, downstream tooling that snapshots the example
    catalogue would hang or crash on import.
    """
    tree = ast.parse(demo.read_text(encoding="utf-8"), filename=str(demo))
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.If)
            and isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__"
            and len(node.test.ops) == 1
            and isinstance(node.test.ops[0], ast.Eq)
            and len(node.test.comparators) == 1
            and isinstance(node.test.comparators[0], ast.Constant)
            and node.test.comparators[0].value == "__main__"
        ):
            return
    pytest.fail(
        f"{demo.name} has no `if __name__ == \"__main__\":` guard; "
        "importing it would execute side effects."
    )
