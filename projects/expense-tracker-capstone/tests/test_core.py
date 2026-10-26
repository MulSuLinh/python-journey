"""Test cho logic và lưu trữ của Expense Tracker."""

import json

import pytest

from expense_tracker.core import (
    add_expense,
    calculate_total,
    create_expense,
    delete_expense,
    filter_by_category,
)
from expense_tracker.storage import load_expenses, save_expenses


def sample_expenses() -> list[dict[str, str | float]]:
    """Tạo dữ liệu mẫu cố định cho các test."""
    return [
        create_expense(20, "Ăn uống", "Bữa trưa", "2026-10-01"),
        create_expense(35.5, "Đi lại", "Xe buýt", "2026-10-02"),
        create_expense(10, "ĂN UỐNG", "Cà phê", "2026-10-03"),
    ]


def test_create_expense_normalizes_text_and_amount() -> None:
    expense = create_expense(12.346, "  Đồ ăn  ", "  Bữa trưa  ", "2026-10-01")

    assert expense["amount"] == 12.35
    assert expense["category"] == "Đồ ăn"
    assert expense["note"] == "Bữa trưa"
    assert expense["date"] == "2026-10-01"


@pytest.mark.parametrize("amount", [0, -1, float("nan"), float("inf"), True])
def test_create_expense_rejects_invalid_amount(amount: float) -> None:
    with pytest.raises(ValueError):
        create_expense(amount, "Ăn uống")


def test_create_expense_rejects_blank_category() -> None:
    with pytest.raises(ValueError):
        create_expense(10, "   ")


@pytest.mark.parametrize("bad_date", ["01/10/2026", "20261001", "2026-2-01"])
def test_create_expense_rejects_invalid_date(bad_date: str) -> None:
    with pytest.raises(ValueError):
        create_expense(10, "Ăn uống", expense_date=bad_date)


def test_add_expense_appends_to_list() -> None:
    expenses: list[dict[str, str | float]] = []
    new_expense = add_expense(expenses, 25, "Đi lại", expense_date="2026-10-01")

    assert expenses == [new_expense]
    assert new_expense["amount"] == 25.0


def test_calculate_total_returns_zero_for_empty_list() -> None:
    assert calculate_total([]) == 0.0


def test_calculate_total_can_filter_by_category() -> None:
    expenses = sample_expenses()

    assert calculate_total(expenses) == 65.5
    assert calculate_total(expenses, "ăn UỐNG") == 30.0


def test_filter_by_category_ignores_case() -> None:
    found = filter_by_category(sample_expenses(), "  ĂN UỐNG ")

    assert len(found) == 2


def test_filter_by_category_rejects_blank_category() -> None:
    with pytest.raises(ValueError):
        filter_by_category(sample_expenses(), " ")


def test_delete_expense_returns_true_when_found() -> None:
    expenses = sample_expenses()
    target_id = str(expenses[0]["id"])

    assert delete_expense(expenses, target_id) is True
    assert len(expenses) == 2
    assert all(expense["id"] != target_id for expense in expenses)


def test_delete_expense_returns_false_when_missing() -> None:
    expenses = sample_expenses()

    assert delete_expense(expenses, "not-found") is False
    assert len(expenses) == 3


def test_missing_json_file_returns_empty_list(tmp_path) -> None:
    assert load_expenses(tmp_path / "not-created.json") == []


def test_save_and_load_expenses_round_trip(tmp_path) -> None:
    path = tmp_path / "nested" / "expenses.json"
    original = sample_expenses()

    save_expenses(path, original)

    assert load_expenses(path) == original


def test_invalid_json_raises_helpful_error(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text("{not valid json", encoding="utf-8")

    with pytest.raises(ValueError, match="JSON"):
        load_expenses(path)


def test_json_must_contain_a_list(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text(json.dumps({"amount": 10}), encoding="utf-8")

    with pytest.raises(ValueError, match="danh sách"):
        load_expenses(path)


def test_json_row_must_have_required_fields(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text(json.dumps([{"id": "one"}]), encoding="utf-8")

    with pytest.raises(ValueError, match="thiếu trường"):
        load_expenses(path)


def test_json_rejects_non_finite_amount(tmp_path) -> None:
    path = tmp_path / "expenses.json"
    path.write_text(
        '[{"id":"one","amount":NaN,"category":"A","note":"","date":"2026-10-01"}]',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Số tiền"):
        load_expenses(path)
