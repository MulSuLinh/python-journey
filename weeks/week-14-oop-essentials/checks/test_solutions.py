"""Focused tests for Week 14 OOP solutions."""

import sys
from pathlib import Path

import pytest

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from solutions.oop_models import (  # noqa: E402
    Animal,
    Bot,
    Dog,
    Progress,
    aggressive,
    balanced,
    defensive,
)


def test_progress_percentage_and_string() -> None:
    progress = Progress(3, 4)

    assert progress.percentage() == 75
    assert str(progress) == "Progress: 3/4 (75%)"


def test_progress_requires_positive_total() -> None:
    with pytest.raises(ValueError, match="positive"):
        Progress(1, 0)


def test_composition_allows_strategy_swap() -> None:
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    bot = Bot(balanced)

    assert bot.choose_action(state) == "right"
    bot.strategy = defensive
    assert bot.choose_action(state) == "right"
    bot.strategy = aggressive
    assert bot.choose_action(state) == "right"


def test_strategy_moves_toward_goal_on_either_side() -> None:
    left_goal = {"position": 3, "opponent_position": 4, "goal": 0}
    right_goal = {"position": 1, "opponent_position": 4, "goal": 4}

    assert Bot(balanced).choose_action(left_goal) == "left"
    assert Bot(balanced).choose_action(right_goal) == "right"


def test_defensive_strategy_waits_near_opponent() -> None:
    state = {"position": 3, "opponent_position": 4, "goal": 0}

    assert Bot(defensive).choose_action(state) == "wait"


def test_aggressive_strategy_uses_goal_direction() -> None:
    state = {"position": 3, "opponent_position": 4, "goal": 0}

    assert Bot(aggressive).choose_action(state) == "left"


def test_dog_inherits_animal_name() -> None:
    dog = Dog("Milo")

    assert isinstance(dog, Animal)
    assert dog.name == "Milo"
    assert dog.speak() == "Milo: woof"
