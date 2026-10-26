"""Giao diện terminal cho ứng dụng theo dõi chi tiêu."""

from pathlib import Path

from expense_tracker.core import (
    add_expense,
    calculate_total,
    delete_expense,
    filter_by_category,
)
from expense_tracker.storage import load_expenses, save_expenses

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.json"


def show_expenses(expenses: list[dict[str, str | float]]) -> None:
    """In danh sách chi tiêu."""
    if not expenses:
        print("Chưa có khoản chi nào.")
        return

    for expense in expenses:
        print(
            f"ID: {expense['id']} | {expense['date']} | "
            f"{expense['category']} | {float(expense['amount']):,.2f} | "
            f"{expense['note']}"
        )


def save_or_warn(expenses: list[dict[str, str | float]]) -> None:
    """Lưu dữ liệu và báo lỗi nếu không ghi được file."""
    try:
        save_expenses(DATA_FILE, expenses)
    except OSError as error:
        print(f"Không lưu được dữ liệu: {error}")


def main() -> None:
    """Chạy menu chính."""
    try:
        expenses = load_expenses(DATA_FILE)
    except (OSError, ValueError) as error:
        print(f"Không đọc được dữ liệu. Hãy kiểm tra file JSON: {error}")
        return

    while True:
        print("\n=== THEO DÕI CHI TIÊU ===")
        print("1. Thêm khoản chi")
        print("2. Xem tất cả khoản chi")
        print("3. Tính tổng chi tiêu")
        print("4. Lọc theo danh mục")
        print("5. Xóa khoản chi")
        print("0. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            try:
                amount = float(input("Số tiền: ").strip())
                category = input("Danh mục: ").strip()
                note = input("Ghi chú: ").strip()
                expense_date = input(
                    "Ngày YYYY-MM-DD (Enter = hôm nay): "
                ).strip()
                expense = add_expense(
                    expenses,
                    amount,
                    category,
                    note,
                    expense_date or None,
                )
                save_or_warn(expenses)
                print(f"Đã thêm khoản chi. ID: {expense['id']}")
            except ValueError as error:
                print(f"Dữ liệu không hợp lệ: {error}")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print(f"Tổng chi tiêu: {calculate_total(expenses):,.2f}")

        elif choice == "4":
            category = input("Nhập danh mục cần lọc: ").strip()
            try:
                matches = filter_by_category(expenses, category)
                show_expenses(matches)
            except ValueError as error:
                print(f"Dữ liệu không hợp lệ: {error}")

        elif choice == "5":
            expense_id = input("Nhập ID cần xóa: ").strip()
            if delete_expense(expenses, expense_id):
                save_or_warn(expenses)
                print("Đã xóa khoản chi.")
            else:
                print("Không tìm thấy ID này.")

        elif choice == "0":
            print("Đã thoát.")
            break

        else:
            print("Lựa chọn không hợp lệ. Hãy chọn từ menu.")


if __name__ == "__main__":
    main()
