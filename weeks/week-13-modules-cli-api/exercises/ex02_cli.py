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


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parser().parse_args()
    print(args)


if __name__ == "__main__":
    main()
