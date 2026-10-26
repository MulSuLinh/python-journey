"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

fixture = b'{"lesson": 13}'


def main() -> None:
    """Check a successful response and handle an unsuccessful status."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print(f"Successful response: {data}")

    try:
        parse_json_response(500, fixture)
    except ValueError as error:
        print(f"Expected error for HTTP 500: {error}")
    else:
        raise AssertionError("HTTP 500 should raise ValueError")


if __name__ == "__main__":
    main()
