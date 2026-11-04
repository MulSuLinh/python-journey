"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    """A bot delegates its decision to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def movement(state: State) -> str:
    position = state.get("position", 0)
    goal = state.get("goal", position)
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    position = state.get("position", 0)
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - position) <= 1:
        return "wait"
    return movement(state)


def balanced(state: State) -> str:
    return movement(state)


def aggressive(state: State) -> str:
    # Aggressive strategy prioritizes reaching the goal over opponent distance.
    return movement(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for strategy in (defensive, balanced, aggressive):
        print(strategy.__name__, "->", Bot(strategy).choose_action(state))

    reverse_state = {"position": 3, "opponent_position": 4, "goal": 0}
    print("reverse:", Bot(aggressive).choose_action(reverse_state))
