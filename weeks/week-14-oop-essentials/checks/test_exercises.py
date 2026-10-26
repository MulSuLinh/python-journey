"""Tests for the learner-facing Week 14 exercise files."""

import importlib.util
from pathlib import Path

import pytest

EXERCISES = Path(__file__).resolve().parents[1] / "exercises"


def load_exercise(filename: str, module_name: str):
    """Load one exercise under a unique module name."""
    spec = importlib.util.spec_from_file_location(
        module_name, EXERCISES / filename
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_progress_percentage_and_string() -> None:
    module = load_exercise("ex01_classes.py", "week14_ex01_classes")
    progress = module.Progress(3, 4)
    assert progress.percentage() == 75
    assert str(progress) == "Progress: 3/4 (75%)"


@pytest.mark.parametrize(
    ("completed", "total"),
    [(1, 0), (-1, 4), (5, 4)],
)
def test_progress_rejects_invalid_values(completed: int, total: int) -> None:
    module = load_exercise("ex01_classes.py", f"week14_progress_{completed}_{total}")
    with pytest.raises(ValueError):
        module.Progress(completed, total)


def test_bot_delegates_to_and_can_swap_strategy() -> None:
    module = load_exercise("ex02_composition.py", "week14_ex02_composition")
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    bot = module.Bot(module.balanced)
    assert bot.choose_action(state) == "right"

    bot.strategy = module.defensive
    assert bot.choose_action(state) == "right"


def test_defensive_strategy_waits_near_opponent() -> None:
    module = load_exercise("ex02_composition.py", "week14_defensive")
    state = {"position": 3, "opponent_position": 4, "goal": 0}
    assert module.Bot(module.defensive).choose_action(state) == "wait"


def test_bot_rejects_non_callable_strategy() -> None:
    module = load_exercise("ex02_composition.py", "week14_invalid_strategy")
    with pytest.raises(TypeError, match="callable"):
        module.Bot(None)


def test_bot_rejects_empty_action() -> None:
    module = load_exercise("ex02_composition.py", "week14_empty_action")
    bot = module.Bot(lambda state: "")
    with pytest.raises(ValueError, match="action"):
        bot.choose_action({"position": 0, "goal": 1})


def test_dog_inherits_name_and_speaks() -> None:
    module = load_exercise("ex03_inheritance.py", "week14_ex03_inheritance")
    dog = module.Dog("Milo")
    assert isinstance(dog, module.Animal)
    assert dog.name == "Milo"
    assert dog.speak() == "Milo: woof"


def test_dog_rejects_blank_name() -> None:
    module = load_exercise("ex03_inheritance.py", "week14_blank_name")
    with pytest.raises(ValueError, match="name"):
        module.Dog("   ")
