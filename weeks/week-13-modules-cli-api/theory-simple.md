# Week 13 — Lý thuyết đơn giản nhất

## 1. Module và package

- **Module**: một file .py chứa code, ví dụ core.py.
- **Package**: một thư mục gom các module, thường có file __init__.py.
- **import**: dùng code ở file khác, tránh viết lại cùng một chức năng nhiều lần.
- **main guard**: chỉ chạy phần demo khi file được chạy trực tiếp, không chạy khi được import.

Ví dụ:

~~~python
from bot_course.core import choose_action

print(choose_action(1, 4))
~~~

## 2. Dependency và môi trường ảo

- **Dependency**: thư viện mà project cần.
- **venv**: tạo môi trường Python riêng cho project.
- Lệnh python -m pip install pytest cài thư viện bằng đúng Python đang được gọi.
- pyproject.toml chứa cấu hình công cụ và dependency của project; không có nghĩa project bắt buộc phải phát hành lên PyPI.

## 3. CLI và argparse

CLI là chương trình điều khiển bằng lệnh trong terminal. argparse giúp đọc các tùy chọn.

~~~python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--turn", type=int, required=True)
args = parser.parse_args()
print(args.turn)
~~~

Chạy bằng lệnh:

~~~bash
python -m solutions.ex02_cli --turn 3
~~~

type=int chuyển chuỗi "3" thành số 3; required=True yêu cầu người dùng cung cấp tham số.

## 4. HTTP và API

- **API**: quy tắc để hai chương trình trao đổi dữ liệu.
- **Request**: yêu cầu client gửi đi.
- **Response**: câu trả lời server gửi về.
- **GET**: phương thức thường dùng để lấy dữ liệu.
- **Status code**: mã kết quả; nhóm 2xx thường là thành công, 4xx thường là lỗi yêu cầu, 5xx thường là lỗi phía server.
- **JSON**: định dạng dữ liệu phổ biến để gửi và nhận.
- **Timeout**: giới hạn thời gian chờ để chương trình không chờ mãi.

Luồng dễ nhớ:

~~~text
Gửi request → nhận status + body → kiểm tra status
→ đọc JSON → kiểm tra dữ liệu → mới sử dụng
~~~

Week 13 dùng dữ liệu mẫu offline. Việc học không cần gửi request tới dịch vụ bên ngoài.

## 5. Adapter

Adapter chuyển đổi dữ liệu giữa hai phần có định dạng khác nhau. Giữ logic cốt lõi tách khỏi CLI và HTTP giúp code dễ thử nghiệm hơn.

## Các lệnh cần nhớ

~~~bash
python -m venv .venv
python -m pip install pytest
python -m solutions.ex02_cli --turn 3
python checks/check_week.py
~~~

## Một câu tóm tắt

**Module chia code, CLI nhận lệnh, API trao đổi dữ liệu, JSON chứa dữ liệu và test kiểm tra hành vi.**
