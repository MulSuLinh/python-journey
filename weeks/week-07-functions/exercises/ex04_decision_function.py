"""Exercise 04 — a deterministic decision function."""


def choose_action(state: str) -> str:
    """Return a deterministic teaching action for ``state``."""
    normalized = state.strip().casefold()
    if normalized == "danger":
        return "defend"
    if normalized == "opportunity":
        return "advance"
    return "wait"


if __name__ == "__main__":
    for state in ("danger", "opportunity", "neutral", ""):
        print(state, "->", choose_action(state))
