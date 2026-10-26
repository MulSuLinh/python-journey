# Expense Tracker — Week 15 Capstone

Một ứng dụng chạy trong terminal để ghi lại chi tiêu cá nhân. Đây là dự án mẫu nhỏ để học cách ghép các kiến thức Python đã học; hãy đọc, chạy, thử lỗi và tự chỉnh sửa trước khi dùng làm bài nộp.

## Chức năng

1. Thêm khoản chi.
2. Xem tất cả khoản chi.
3. Tính tổng chi tiêu.
4. Lọc khoản chi theo danh mục.
5. Xóa khoản chi theo ID.
6. Tự lưu dữ liệu vào file JSON để lần sau mở lại vẫn còn.

## Setup — chuẩn bị

Cần Python 3.12 trở lên. Dự án dùng thư viện có sẵn của Python; chỉ cần cài pytest nếu máy chưa có.

~~~bash
python --version
python -m pip install pytest
~~~

## Usage — chạy chương trình

Mở terminal tại thư mục projects/expense-tracker-capstone trong repository, sau đó chạy:

~~~bash
python main.py
~~~

Chọn số trên menu và làm theo hướng dẫn. File dữ liệu sẽ được tạo tự động tại data/expenses.json sau khi lưu khoản chi đầu tiên.

Ví dụ dữ liệu được lưu:

~~~json
[
  {
    "id": "a1b2c3d4",
    "amount": 25000.0,
    "category": "Ăn uống",
    "note": "Bữa trưa",
    "date": "2026-10-26"
  }
]
~~~

ID thực tế được tạo tự động, nên sẽ khác ví dụ trên.

## Test — chạy kiểm thử

Từ thư mục dự án, chạy:

~~~bash
python -m pytest
~~~

Các test kiểm tra thêm khoản chi, số tiền sai, tính tổng, lọc danh mục, xóa giao dịch và lưu/đọc JSON. Test lưu file vào thư mục tạm để không đụng đến dữ liệu thật.

## Cấu trúc

- main.py: menu và giao tiếp với người dùng.
- expense_tracker/core.py: quy tắc xử lý chi tiêu.
- expense_tracker/storage.py: đọc và ghi JSON.
- tests/test_core.py: kiểm tra logic và lưu trữ.
- AI_USAGE.md: ghi rõ AI đã hỗ trợ phần nào và phần người học cần tự xác minh.

## Quyết định thiết kế

- Dùng list để chứa nhiều giao dịch; mỗi giao dịch là một dict.
- Dùng JSON vì dữ liệu nhỏ và dễ đọc.
- Tách logic khỏi input/print để có thể test mà không cần nhập tay.
- Dùng hàm thay vì tạo class không cần thiết.
- Ngày được lưu theo định dạng YYYY-MM-DD; số tiền phải lớn hơn 0.

## Evidence

Chạy test bằng lệnh ở phần Test. Trước khi nộp, hãy chạy chương trình bằng tay, thử input không hợp lệ và ghi kết quả thực tế của bạn tại đây.

- Tests: cần chạy và điền kết quả thực tế.
- Debugging: hãy ghi lại một lỗi bạn đã tái hiện và sửa.
- Git: nên chia thay đổi thành các commit nhỏ, có ý nghĩa.

## Known limitations — giới hạn hiện tại

- Đây là ứng dụng terminal, chưa có giao diện đồ họa.
- Chưa hỗ trợ nhiều người dùng hoặc nhiều loại tiền tệ.
- Nếu file JSON bị sửa sai cấu trúc, chương trình báo lỗi để người dùng biết; cần sửa file trước khi dùng tiếp.
- Số tiền dùng float để phù hợp bài học nhập môn; ứng dụng tài chính thực tế nên cân nhắc Decimal.

## AI usage

Xem AI_USAGE.md. Không nộp nguyên trạng chỉ vì chương trình chạy được: hãy tự giải thích từng hàm và kiểm chứng kết quả.
