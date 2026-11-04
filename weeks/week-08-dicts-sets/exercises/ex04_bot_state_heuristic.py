"""Exercise 04: structured course-local state → heuristic action."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Chọn một action local bằng 2–4 rules dễ giải thích."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    if position == goal:
        return "wait"
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - position) <= 1:
        return "wait"
    return "right" if position < goal else "left"


def main() -> None:
    state = {
        "turn": 1, "max_turns": 6, "position": 0,
        "opponent_position": 4, "goal": 4,
        "min_position": 0, "max_position": 4,
    }
    action = choose_action(state)
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(f"action={action}, legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
