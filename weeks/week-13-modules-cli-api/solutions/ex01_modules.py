"""Solution 01: import a module and run behavior behind a main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Run one local example so importing this module has no side effects."""
    position = 1
    goal = 4
    action = choose_action(position, goal)
    print(f"Vị trí: {position}; mục tiêu: {goal}; hành động: {action}")


if __name__ == "__main__":
    main()
