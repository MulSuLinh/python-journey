# Week 13 — Lời giải tham khảo

Các file trong thư mục này là lời giải để đối chiếu sau khi tự làm starter exercises. Chúng không thay thế việc hiểu code.

Chạy từ thư mục tuần:

~~~bash
cd weeks/week-13-modules-cli-api
python -m solutions.ex01_modules
python -m solutions.ex02_cli --turn 3
python -m solutions.ex03_http
~~~

## File nào giải bài nào?

- ex01_modules.py: import hàm từ module khác; đặt lời gọi hàm bên trong main() và main guard.
- ex02_cli.py: dùng argparse để đọc --turn thành số nguyên.
- ex03_http.py: parse JSON response mẫu, kiểm tra dữ liệu và từ chối status 500. Không gọi mạng thật.

## Tự kiểm tra

~~~bash
python -m pytest checks/test_solutions.py
python checks/check_week.py
~~~

pytest và checker chỉ giúp phát hiện một số lỗi. Hãy đọc từng dòng và thử sửa một giá trị để hiểu vì sao kết quả thay đổi.
