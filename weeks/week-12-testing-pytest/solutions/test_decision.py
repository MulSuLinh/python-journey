"""Lời giải tham khảo cho các test Week 12."""

import pytest

from exercises.decision import choose_action, validate_turn


def test_normal_case_moves_toward_goal() -> None:
    assert choose_action(1, 4) == "right"


def test_edge_case_waits_at_goal() -> None:
    assert choose_action(4, 4) == "wait"


def test_invalid_turn_raises_value_error() -> None:
    with pytest.raises(ValueError, match="positive"):
        validate_turn(0)


def test_regression_position_past_goal_moves_left() -> None:
    assert choose_action(4, 1) == "left"
