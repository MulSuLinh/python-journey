"""Focused tests for Week 13 example solutions."""

import sys
from pathlib import Path

import pytest

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.core import choose_action  # noqa: E402
from bot_course.http_foundation import parse_json_response  # noqa: E402
from solutions.ex02_cli import parse_args  # noqa: E402
from solutions.ex03_http import check_error_status, inspect_fixture  # noqa: E402


def test_core_is_importable_and_returns_action() -> None:
    assert choose_action(1, 4) == "right"
    assert choose_action(4, 1) == "left"
    assert choose_action(3, 3) == "wait"


def test_cli_parses_integer_argument() -> None:
    assert parse_args(["--turn", "3"]).turn == 3


def test_cli_rejects_missing_required_argument() -> None:
    with pytest.raises(SystemExit):
        parse_args([])


def test_successful_fixture_is_parsed() -> None:
    assert inspect_fixture()["lesson"] == 13


def test_error_status_is_rejected() -> None:
    with pytest.raises(ValueError, match="status"):
        parse_json_response(500, b'{"error": true}')


def test_solution_error_check_runs() -> None:
    check_error_status()


def test_malformed_json_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_json_response(200, b"not-json")
