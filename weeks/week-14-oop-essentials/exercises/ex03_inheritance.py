"""Exercise 03: one clear basic inheritance example."""


class Animal:
    """Base class that stores the animal's name."""

    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    """A dog is an animal, so it inherits Animal's name attribute."""

    def speak(self) -> str:
        """Return the dog's sound."""
        return f"{self.name}: woof"


def main() -> None:
    dog = Dog("Milo")
    print(dog.speak())
    print("Dog is an Animal because Dog inherits from the Animal class.")


if __name__ == "__main__":
    main()
