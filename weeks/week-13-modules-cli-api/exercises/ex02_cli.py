"""Exercise 02: parse a required integer option with argparse."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    result = argparse.ArgumentParser(
        description="Demo CLI that accepts a turn number."
    )
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="Turn number (integer).",
    )
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse arguments; argv can be supplied by tests."""
    return parser().parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parse_args(argv)
    print(args)


if __name__ == "__main__":
    main()
