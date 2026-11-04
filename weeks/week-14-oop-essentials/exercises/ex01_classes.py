"""Exercise 01: class, object and methods."""


class Progress:
    """Represent progress through a fixed number of tasks."""

    def __init__(self, completed: int, total: int):
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")
        if not 0 <= completed <= total:
            raise ValueError("completed phải nằm trong khoảng 0..total")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


if __name__ == "__main__":
    progress = Progress(3, 4)
    print(progress.percentage())
    print(progress)
