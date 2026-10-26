"""Logic chính của Expense Tracker, tách khỏi giao diện terminal."""

from datetime import date
from math import isfinite
from uuid import uuid4

Expense = dict[str, str | float]


def create_expense(
    amount: float,
    category: str,
    note: str = "",
    expense_date: str | None = None,
) -> Expense:
    """Tạo khoản chi hợp lệ và trả về dict mới."""
    if isinstance(amount, bool):
        raise ValueError("Số tiền phải là một con số.")

    try:
        amount = float(amount)
    except (TypeError, ValueError) as error:
        raise ValueError("Số tiền phải là một con số.") from error

    if not isfinite(amount) or amount <= 0:
        raise ValueError("Số tiền phải lớn hơn 0.")

    amount = round(amount, 2)
    if amount <= 0:
        raise ValueError("Số tiền nhỏ nhất là 0.01.")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Danh mục không được để trống.")

    if not isinstance(note, str):
        raise ValueError("Ghi chú phải là văn bản.")

    category = category.strip()
    note = note.strip()

    if expense_date is None or (
        isinstance(expense_date, str) and not expense_date.strip()
    ):
        expense_date = date.today().isoformat()

    if not isinstance(expense_date, str):
        raise ValueError("Ngày phải đúng định dạng YYYY-MM-DD.")

    try:
        parsed_date = date.fromisoformat(expense_date)
    except ValueError as error:
        raise ValueError("Ngày phải đúng định dạng YYYY-MM-DD.") from error

    if parsed_date.isoformat() != expense_date:
        raise ValueError("Ngày phải đúng định dạng YYYY-MM-DD.")

    return {
        "id": uuid4().hex[:8],
        "amount": amount,
        "category": category,
        "note": note,
        "date": expense_date,
    }


def add_expense(
    expenses: list[Expense],
    amount: float,
    category: str,
    note: str = "",
    expense_date: str | None = None,
) -> Expense:
    """Tạo khoản chi hợp lệ, thêm vào danh sách và trả về khoản đó."""
    expense = create_expense(amount, category, note, expense_date)
    expenses.append(expense)
    return expense


def calculate_total(
    expenses: list[Expense],
    category: str | None = None,
) -> float:
    """Tính tổng mọi khoản chi hoặc chỉ một danh mục."""
    if category is not None:
        category = category.strip().casefold()

    total = sum(
        float(expense["amount"])
        for expense in expenses
        if category is None
        or str(expense["category"]).casefold() == category
    )
    return round(total, 2)


def filter_by_category(
    expenses: list[Expense],
    category: str,
) -> list[Expense]:
    """Lọc giao dịch theo danh mục, không phân biệt chữ hoa/chữ thường."""
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Danh mục không được để trống.")

    wanted = category.strip().casefold()
    return [
        expense
        for expense in expenses
        if str(expense["category"]).casefold() == wanted
    ]


def delete_expense(expenses: list[Expense], expense_id: str) -> bool:
    """Xóa theo ID; trả True nếu tìm thấy, nếu không thì trả False."""
    for index, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            del expenses[index]
            return True
    return False
