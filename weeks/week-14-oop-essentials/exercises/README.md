# Chạy exercises Week 14

Chạy từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
python -m pytest weeks/week-14-oop-essentials/checks
```

## Nội dung

- `ex01_classes.py`: tạo object, tính phần trăm tiến độ và kiểm tra dữ liệu hợp lệ.
- `ex02_composition.py`: `Bot` nhận một strategy, gọi strategy và cho phép thay strategy.
- `ex03_inheritance.py`: `Dog` kế thừa `Animal`, dùng lại thuộc tính `name`.

Bộ test trong `checks/test_exercises.py` kiểm tra trực tiếp các exercise. Bộ
`checks/test_solutions.py` kiểm tra lời giải tham khảo riêng; hai bộ test có
mục đích khác nhau.
