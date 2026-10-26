"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

FIXTURE = b'{"lesson": 13}'


def inspect_fixture() -> dict[str, object]:
    """Parse the successful static response fixture."""
    return parse_json_response(200, FIXTURE)


def check_error_status() -> None:
    """Confirm that an unsuccessful status is rejected."""
    try:
        parse_json_response(500, FIXTURE)
    except ValueError as error:
        if "status" not in str(error).lower():
            raise
    else:
        raise AssertionError("HTTP 500 should raise ValueError")


def main() -> None:
    """Show successful JSON parsing and expected error handling."""
    data = inspect_fixture()
    assert data["lesson"] == 13
    print(f"Successful response: {data}")

    check_error_status()
    print("Expected error for HTTP 500 was handled.")


if __name__ == "__main__":
    main()
