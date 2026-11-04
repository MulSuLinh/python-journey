# Week 12 — Lời giải tham khảo

Bài tuần này luyện cách viết test mô tả hành vi mong đợi. Không cần sửa code trong `exercises/decision.py`: phần đó là logic mà test sẽ kiểm tra.

## Đáp án cho bốn trường hợp

~~~python
import pytest
from exercises.decision import choose_action, validate_turn


def test_normal_case_moves_toward_goal():
    assert choose_action(1, 4) == "right"


def test_edge_case_waits_at_goal():
    assert choose_action(4, 4) == "wait"


def test_invalid_turn_raises_value_error():
    with pytest.raises(ValueError):
        validate_turn(0)


def test_regression_position_past_goal_moves_left():
    assert choose_action(4, 1) == "left"
~~~

## Vì sao các test này đúng?

- **Normal case:** vị trí 1 nhỏ hơn mục tiêu 4 nên bot đi sang phải.
- **Edge case:** vị trí bằng mục tiêu nên bot chờ.
- **Invalid case:** lượt 0 không hợp lệ nên hàm phải báo `ValueError`.
- **Regression case:** vị trí 4 lớn hơn mục tiêu 1 nên bot phải đi sang trái. Test này bắt lỗi nếu chương trình luôn trả về `right`.

## Chạy bài

Từ thư mục gốc repository:

~~~bash
python -m pytest weeks/week-12-testing-pytest/tests -q
python weeks/week-12-testing-pytest/checks/check_week.py
~~~

Một test PASS chỉ chứng minh hành vi được test đang đúng với expected value đó; nó không chứng minh toàn bộ chương trình không còn lỗi.
