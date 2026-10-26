# Ôn lý thuyết Python — bản đơn giản nhất

Mục tiêu: hiểu chương trình làm gì, không phải học thuộc mọi cú pháp.

## Tuần 1 — Chạy chương trình và Git

- Python: ngôn ngữ dùng để viết chỉ dẫn cho máy tính.
- Terminal: nơi gõ lệnh để chạy chương trình.
- File .py: file chứa code Python.
- Git: lưu lịch sử các lần thay đổi code.
- GitHub: nơi lưu repository online.
- Commit: một mốc lưu thay đổi; push: gửi commit lên GitHub.

## Tuần 2 — Biến và kiểu dữ liệu

Biến là chiếc hộp đặt tên cho dữ liệu.

~~~python
name = "Linh"
age = 18
price = 12.5
is_ready = True
~~~

- int: số nguyên; float: số thập phân.
- str: văn bản; bool: đúng hoặc sai.
- input() nhận dữ liệu từ bàn phím và luôn trả về chuỗi.
- int() hoặc float() đổi chuỗi sang số; conversion có thể lỗi.
- print() in kết quả ra màn hình.

## Tuần 3 — Điều kiện

Dùng if/elif/else để chương trình chọn việc cần làm.

~~~python
if score >= 5:
    print("Đạt")
else:
    print("Chưa đạt")
~~~

- == so sánh bằng; != khác; > lớn hơn; < nhỏ hơn.
- and: cả hai điều kiện đúng; or: ít nhất một đúng; not: đảo đúng/sai.
- Kiểm tra dữ liệu trước khi dùng để tránh input sai.

## Tuần 4 — Chuỗi

Chuỗi là văn bản, ví dụ "hello".

- name.strip(): bỏ khoảng trắng ở hai đầu.
- name.lower(): đổi chữ thành chữ thường.
- text.split(): tách chuỗi thành danh sách.
- "Xin chào " + name: nối chuỗi.
- f-string giúp chèn biến vào câu: f"Xin chào {name}".
- Regex dùng tìm mẫu văn bản; chỉ dùng khi các hàm chuỗi bình thường chưa đủ.

## Tuần 5 — List và tuple

- list: danh sách có thứ tự và có thể sửa.
- tuple: nhóm giá trị có thứ tự, thường không sửa sau khi tạo.
- items.append(x): thêm phần tử vào cuối list.
- items[index]: lấy phần tử theo vị trí, vị trí đầu là 0.
- len(items): số phần tử; items[0:2]: lấy một đoạn.
- Mutable nghĩa là có thể sửa sau khi tạo; immutable nghĩa là không sửa trực tiếp được.

## Tuần 6 — Vòng lặp

Vòng lặp dùng để làm một việc nhiều lần.

~~~python
for item in items:
    print(item)
~~~

- for: đi qua từng phần tử.
- while: lặp khi điều kiện còn đúng.
- break: dừng vòng lặp; continue: bỏ qua lượt hiện tại.
- enumerate(items): lấy cả vị trí lẫn phần tử.
- zip(a, b): đi qua hai danh sách cùng lúc.
- Comprehension tạo list mới gọn gàng khi logic đơn giản.

## Tuần 7 — Hàm

Hàm là một phần chương trình được đặt tên để tái sử dụng.

~~~python
def add(a: float, b: float) -> float:
    return a + b
~~~

- Parameter: tên biến nhận dữ liệu vào hàm.
- Argument: giá trị truyền vào khi gọi hàm.
- return: trả kết quả về nơi gọi hàm.
- Scope: nơi một biến có thể được dùng.
- Type hint nói rõ kiểu dữ liệu dự định dùng; nó không tự động chặn mọi dữ liệu sai khi chạy.

## Tuần 8 — Dict và set

- dict: lưu dữ liệu theo cặp khóa → giá trị, ví dụ student["name"].
- dict.get("age", 0): lấy giá trị hoặc dùng giá trị mặc định.
- set: tập hợp phần tử không trùng nhau.
- Chọn list khi cần danh sách có thứ tự; dict khi cần tìm bằng khóa; set khi cần loại trùng.

## Tuần 9 — Midterm Project

Không có cú pháp mới quan trọng. Ghép biến, điều kiện, chuỗi, list/dict, vòng lặp và hàm thành một chương trình nhỏ. Chia việc lớn thành các bước nhỏ và có README.

## Tuần 10 — File, pathlib, CSV, JSON

- File giúp lưu dữ liệu sau khi chương trình đóng.
- pathlib.Path biểu diễn đường dẫn file/thư mục.
- with open(...) giúp đóng file đúng cách sau khi làm xong.
- CSV phù hợp dữ liệu dạng bảng.
- JSON phù hợp dữ liệu dạng list/dict.
- Đọc file có thể gặp file chưa tồn tại hoặc dữ liệu bị hỏng.

Ví dụ JSON:

~~~json
[
  {"category": "Ăn uống", "amount": 25000}
]
~~~

## Tuần 11 — Exception và debug

- Exception là lỗi phát sinh khi chương trình chạy.
- try: thử chạy; except: xử lý loại lỗi dự đoán được.
- raise: chủ động báo rằng dữ liệu hoặc thao tác không hợp lệ.
- Traceback cho biết đường đi dẫn đến lỗi; đọc dòng cuối và tìm dòng trong code liên quan.
- Đừng dùng except trống để che tất cả lỗi.

Cách debug dễ nhớ:

~~~text
Tái hiện lỗi → đọc thông báo → tìm dòng lỗi → sửa → chạy lại
~~~

## Tuần 12 — Test với pytest

Test là đoạn code tự kiểm tra hành vi của chương trình.

~~~python
def test_addition():
    assert 2 + 3 == 5
~~~

- assert: điều kiện nào sai thì test thất bại.
- Normal case: dữ liệu thường.
- Edge case: ranh giới, danh sách rỗng hoặc giá trị nhỏ nhất/lớn nhất.
- Invalid input: dữ liệu không hợp lệ.
- Test giúp phát hiện lỗi; test PASS không chứng minh mọi tình huống đều đúng.

## Tuần 13 — Module, CLI, API

- Module: file Python có thể import để dùng lại.
- import: dùng code từ module khác.
- venv: môi trường Python riêng cho dự án.
- dependency: thư viện mà dự án cần.
- CLI: chương trình nhận lệnh/tham số từ terminal.
- API: cách chương trình trao đổi dữ liệu với dịch vụ khác.
- HTTP GET thường dùng để lấy dữ liệu; status code cho biết kết quả yêu cầu.
- JSON response là dữ liệu trả về có cấu trúc; hãy kiểm tra dữ liệu trước khi dùng.

## Tuần 14 — OOP cơ bản

- Class: bản mô tả để tạo đối tượng.
- Object: một thứ cụ thể tạo từ class.
- __init__: hàm khởi tạo dữ liệu cho object.
- self: object hiện tại.
- Attribute: dữ liệu nằm trong object; method: hàm thuộc class.
- Dùng class khi nó làm mô hình rõ hơn; không cần tạo class cho mọi thứ.
- Composition: một object chứa/sử dụng object khác.
- Inheritance: một class kế thừa class khác; chỉ dùng khi quan hệ đó tự nhiên.

## Tuần 15 — Capstone

Capstone là bài tổng hợp: giải quyết một vấn đề, có ít nhất 4 chức năng có ý nghĩa, chia code thành hàm/module, xử lý lỗi, có ít nhất 5 test, README, AI_USAGE.md và lịch sử Git dễ hiểu.

## Từ khóa dễ nhớ

- Biến: giữ dữ liệu.
- if: lựa chọn.
- for/while: lặp lại.
- list/dict/set: cách gom dữ liệu.
- def/return: đóng gói và trả kết quả.
- file/JSON: lưu dữ liệu.
- try/except: xử lý lỗi dự kiến.
- pytest/assert: kiểm tra chương trình.
- import/module: chia code thành file.
- class/object: mô hình hóa dữ liệu và hành vi.
- Git/commit: lưu lại từng mốc thay đổi.

## Công thức làm dự án

~~~text
Hiểu vấn đề
→ chia thành chức năng nhỏ
→ viết code
→ chạy thử
→ test cả dữ liệu sai
→ sửa lỗi
→ ghi hướng dẫn README
→ commit lên GitHub
→ giải thích được code của mình
~~~

Nguồn yêu cầu capstone chính thức: [FINAL_PROJECT.md](../../FINAL_PROJECT.md).
