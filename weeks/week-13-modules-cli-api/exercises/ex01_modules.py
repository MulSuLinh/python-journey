"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Run a small example without side effects when this module is imported."""
    position = 1
    goal = 4
    action = choose_action(position, goal)
    print(f"Vị trí: {position}; mục tiêu: {goal}; hành động: {action}")


if __name__ == "__main__":
    main()
