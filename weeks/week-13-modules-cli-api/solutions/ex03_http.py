"""Solution 03: parse offline HTTP response fixtures without network access."""

from bot_course.http_foundation import parse_json_response

SUCCESS_FIXTURE = b'{"lesson": 13, "topic": "HTTP"}'


def inspect_fixture() -> dict[str, object]:
    """Parse a successful static JSON response and check its key."""
    result = parse_json_response(200, SUCCESS_FIXTURE)
    assert result["lesson"] == 13
    return result


def check_error_status() -> None:
    """Reject a server-error status instead of treating it as success."""
    try:
        parse_json_response(500, b'{"error": "demo"}')
    except ValueError:
        return
    raise AssertionError("HTTP status 500 must be rejected")


def main() -> None:
    result = inspect_fixture()
    check_error_status()
    print(result)
    print("Đã kiểm tra response thành công và status lỗi.")


if __name__ == "__main__":
    main()
