"""Exercise 02: compose Bot with a replaceable strategy."""

from collections.abc import Callable, Mapping

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Choose actions by delegating to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        if not callable(strategy):
            raise TypeError("strategy must be callable")
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Ask the current strategy to choose an action."""
        if not isinstance(state, dict):
            raise TypeError("state must be a dictionary")
        action = self.strategy(state)
        if not isinstance(action, str) or not action:
            raise ValueError("strategy must return a non-empty action string")
        return action


def move_toward_goal(state: dict[str, int]) -> str:
    """Move left or right toward the goal, or wait if already there."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    """Wait when the opponent is nearby; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    """Use the goal direction as a balanced default."""
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    """Move directly toward the goal."""
    return move_toward_goal(state)


def main() -> None:
    """Demonstrate strategy composition and switching behavior."""
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    bot = Bot(balanced)
    print(f"Balanced: {bot.choose_action(state)}")

    # Swap behavior without changing the Bot class.
    bot.strategy = defensive
    print(f"Defensive: {bot.choose_action(state)}")
    bot.strategy = aggressive
    print(f"Aggressive: {bot.choose_action(state)}")

    reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}
    print(f"Moving toward goal 0: {Bot(balanced).choose_action(reverse_state)}")


if __name__ == "__main__":
    main()
