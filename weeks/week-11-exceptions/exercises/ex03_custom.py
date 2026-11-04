"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    """Return the absolute distance between two positions."""
    result = abs(position - goal)
    assert result >= 0
    return result


if __name__ == "__main__":
    assert distance(1, 4) == 3
    print(distance(1, 4))
