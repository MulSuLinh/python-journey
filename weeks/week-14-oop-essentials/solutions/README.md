# Week 14 — Lời giải tham khảo

Các lời giải chính được gom trong `oop_models.py` để tránh lặp code giữa nhiều bài.

## Bài 1 — Class và object

`Progress` lưu số phần đã hoàn thành và tổng số phần. `percentage()` tính phần trăm; `__str__()` tạo nội dung dễ đọc khi dùng `print()`.

Ví dụ: `Progress(3, 4)` tương ứng 3/4 phần, tức 75%.

## Bài 2 — Composition

`Bot` nhận một strategy (hàm quyết định) khi khởi tạo. `choose_action()` giao việc chọn hành động cho strategy đó. Có thể đổi từ `balanced` sang `defensive` hoặc `aggressive` mà không sửa class `Bot`.

## Bài 3 — Inheritance

`Dog` kế thừa `Animal`, nên object `Dog` có sẵn thuộc tính `name`. `speak()` là hành vi riêng của `Dog`.

## Chạy và kiểm tra

Chạy từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
python -m pytest weeks/week-14-oop-essentials/checks/test_solutions.py
```

Hãy thử thay dữ liệu để kiểm tra cả ba trường hợp: mục tiêu ở bên phải, mục tiêu ở bên trái và bot đã tới mục tiêu. Đọc code trước khi chạy và tự giải thích được `self`, `__init__`, composition và inheritance.
