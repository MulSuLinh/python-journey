"""Exercise 01: imports, modules and the main guard."""

from bot_course.core import choose_action


def example_action(position: int = 1, goal: int = 4) -> str:
    """Return the action chosen by the course-local decision core."""
    return choose_action(position, goal)


def main() -> None:
    """Run a small example without side effects when this module is imported."""
    position = 1
    goal = 4
    action = example_action(position, goal)
    print(f"Vị trí: {position}; mục tiêu: {goal}; hành động: {action}")


if __name__ == "__main__":
    main()
