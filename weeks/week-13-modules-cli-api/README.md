# Tuần 13 — Modules · Packages · Dependencies · CLI · API/HTTP

Tuần này bạn học cách chia chương trình thành module/package, tạo CLI nhỏ và hiểu request/response HTTP qua ví dụ offline trung lập.

## Lý thuyết và bài tập

- [Lý thuyết đơn giản nhất](theory-simple.md).
- [Notes chi tiết](notes.md).
- [Exercises đang làm](exercises/README.md).
- [Lời giải tham khảo](solutions/README.md).
- [Hints](hints.md).

## Chạy ví dụ chính

Từ thư mục gốc repository:

~~~bash
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/checks/check_week.py
python -m pytest weeks/week-13-modules-cli-api/checks/test_solutions.py
~~~

Để chạy các exercise/solution có import package, vào thư mục tuần và dùng module mode:

~~~bash
cd weeks/week-13-modules-cli-api
python -m solutions.ex01_modules
python -m solutions.ex02_cli --turn 3
python -m solutions.ex03_http
~~~

## Mục tiêu tuần

- Import module chuẩn và module tự viết.
- Hiểu __init__.py, main guard, venv và dependency.
- Đọc tham số bằng argparse.
- Hiểu HTTP GET, status code, JSON response, timeout và network error.
- Giữ core logic tách khỏi CLI/transport.

Core checks không gọi mạng và không dùng endpoint production. Adapter trong khóa là mô hình học tập; không suy đoán endpoint/auth/schema của dịch vụ bên ngoài.

## Mini-project

[Local Bot CLI and Adapter Boundary](mini-project/README.md): CLI gọi course-local core, HTTP chỉ dùng static fixture.
