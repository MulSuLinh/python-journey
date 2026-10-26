# Tuần 14 — OOP Essentials · Composition · Basic inheritance

Tuần này bạn gom state và behavior có cùng trách nhiệm vào object. Với bot, composition là lựa chọn chính: Bot nhận một strategy có thể thay thế.

## Lý thuyết và bài tập

- [Lý thuyết OOP đơn giản nhất](theory-simple.md).
- [Notes chi tiết](notes.md).
- [Examples](examples/).
- [Exercises để tự làm](exercises/).
- [Lời giải tham khảo](solutions/README.md).
- [Hints](hints.md).

## Chạy ví dụ và kiểm tra

Từ thư mục gốc repository:

~~~bash
python weeks/week-14-oop-essentials/examples/01_class_object.py
python weeks/week-14-oop-essentials/examples/02_composition.py
python weeks/week-14-oop-essentials/examples/03_basic_inheritance.py
python weeks/week-14-oop-essentials/checks/check_week.py
python -m pytest weeks/week-14-oop-essentials/checks/test_solutions.py
~~~

## Mục tiêu tuần

- Tạo class, object, __init__, instance attributes, methods và __str__.
- Hiểu encapsulation là giữ một trách nhiệm cùng dữ liệu liên quan.
- Dùng composition trước inheritance.
- Đổi defensive/balanced/aggressive strategy mà không sửa arena core.
- Dùng basic inheritance khi quan hệ is-a thật rõ.

## Mini-project

[Strategy Composition](mini-project/README.md): tạo Bot nhận strategy qua __init__, sau đó so sánh ba hành vi trên cùng một state. Kiểm tra mục tiêu ở cả hai phía.
