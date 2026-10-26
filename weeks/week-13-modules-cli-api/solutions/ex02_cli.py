"""Solution 02: parse a required integer argument with argparse."""

import argparse


def parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    result = argparse.ArgumentParser(description="Demo CLI argument")
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="số lượt hiện tại",
    )
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse arguments; argv can be supplied by a test."""
    return parser().parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Display the parsed arguments."""
    args = parse_args(argv)
    print(f"Turn: {args.turn}")


if __name__ == "__main__":
    main()
