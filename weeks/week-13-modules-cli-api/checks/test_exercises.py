"""Tests for the learner-facing Week 13 exercise files."""

import importlib.util
from pathlib import Path

import pytest

WEEK_ROOT = Path(__file__).resolve().parents[1]
EXERCISES = WEEK_ROOT / "exercises"


def load_exercise(filename: str, module_name: str):
    """Load one exercise under a unique name to avoid package collisions."""
    import sys

    week_root = str(WEEK_ROOT)
    if week_root not in sys.path:
        sys.path.insert(0, week_root)
    spec = importlib.util.spec_from_file_location(
        module_name, EXERCISES / filename
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_module_exercise_reuses_course_core() -> None:
    module = load_exercise("ex01_modules.py", "week13_ex01_modules")
    assert module.example_action(1, 4) == "right"
    assert module.example_action(4, 1) == "left"
    assert module.example_action(3, 3) == "wait"


def test_cli_parses_integer_argument() -> None:
    module = load_exercise("ex02_cli.py", "week13_ex02_cli")
    assert module.parse_args(["--turn", "3"]).turn == 3


def test_cli_rejects_non_integer_argument() -> None:
    module = load_exercise("ex02_cli.py", "week13_ex02_cli_invalid")
    with pytest.raises(SystemExit):
        module.parse_args(["--turn", "later"])


def test_cli_requires_turn_argument() -> None:
    module = load_exercise("ex02_cli.py", "week13_ex02_cli_missing")
    with pytest.raises(SystemExit):
        module.parse_args([])


def test_http_exercise_parses_static_fixture() -> None:
    module = load_exercise("ex03_http.py", "week13_ex03_http")
    assert module.inspect_fixture() == {"lesson": 13}


def test_http_exercise_rejects_error_status() -> None:
    module = load_exercise("ex03_http.py", "week13_ex03_http_error")
    module.check_error_status()
    with pytest.raises(ValueError, match="status"):
        module.parse_json_response(503, b'{"error": true}')


def test_http_parser_rejects_malformed_json() -> None:
    module = load_exercise("ex03_http.py", "week13_ex03_http_bad_json")
    with pytest.raises(ValueError):
        module.parse_json_response(200, b"not-json")
