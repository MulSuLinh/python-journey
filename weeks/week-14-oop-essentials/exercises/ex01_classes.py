"""Exercise 01: class, object and methods."""


class Progress:
    """Store completed work and report progress as a percentage."""

    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Return the percentage of completed work."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Return a short, readable summary."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


def main() -> None:
    """Create an object and show its data and behavior."""
    progress = Progress(3, 4)
    print(progress.percentage())
    print(progress)


if __name__ == "__main__":
    main()
