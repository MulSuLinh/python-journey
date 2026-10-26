"""Đọc và ghi danh sách chi tiêu dưới dạng JSON."""

import json
from datetime import date
from math import isfinite
from pathlib import Path

from .core import Expense


def load_expenses(path: Path) -> list[Expense]:
    """Đọc JSON; file chưa có thì trả về danh sách rỗng."""
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError("File JSON không hợp lệ hoặc không đọc được.") from error

    if not isinstance(data, list):
        raise ValueError("Dữ liệu phải là một danh sách.")

    expenses: list[Expense] = []
    required_fields = {"id", "amount", "category", "note", "date"}

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict) or not required_fields.issubset(item):
            raise ValueError(f"Khoản chi thứ {index} thiếu trường dữ liệu.")

        expense_id = item["id"]
        amount = item["amount"]
        category = item["category"]
        note = item["note"]
        expense_date = item["date"]

        if not isinstance(expense_id, str) or not expense_id.strip():
            raise ValueError(f"ID ở khoản chi thứ {index} không hợp lệ.")
        if isinstance(amount, bool) or not isinstance(amount, int | float):
            raise ValueError(f"Số tiền ở khoản chi thứ {index} không hợp lệ.")
        if not isfinite(amount) or amount <= 0:
            raise ValueError(f"Số tiền ở khoản chi thứ {index} phải lớn hơn 0.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"Danh mục ở khoản chi thứ {index} không hợp lệ.")
        if not isinstance(note, str):
            raise ValueError(f"Ghi chú ở khoản chi thứ {index} không hợp lệ.")
        if not isinstance(expense_date, str):
            raise ValueError(f"Ngày ở khoản chi thứ {index} không hợp lệ.")

        try:
            parsed_date = date.fromisoformat(expense_date)
        except ValueError as error:
            raise ValueError(
                f"Ngày ở khoản chi thứ {index} phải theo YYYY-MM-DD."
            ) from error

        if parsed_date.isoformat() != expense_date:
            raise ValueError(
                f"Ngày ở khoản chi thứ {index} phải theo YYYY-MM-DD."
            )

        expenses.append(
            {
                "id": expense_id,
                "amount": round(float(amount), 2),
                "category": category.strip(),
                "note": note,
                "date": expense_date,
            }
        )

    return expenses


def save_expenses(path: Path, expenses: list[Expense]) -> None:
    """Tạo thư mục cha nếu cần và ghi danh sách ra file JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(expenses, ensure_ascii=False, indent=2, allow_nan=False)
    path.write_text(content + "\n", encoding="utf-8")
