# Chạy exercises Week 13

Các exercise import package `bot_course`, vì vậy hãy chạy chúng theo module
mode từ thư mục của tuần:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
```

Module mode đặt week root vào import path. Nếu chạy trực tiếp
`python exercises/ex03_http.py`, Python chỉ nhìn thấy thư mục `exercises/` và
không tìm được package sibling `bot_course`.

Chạy test trực tiếp cho cả exercise và lời giải tham khảo từ repository root:\n\n```bash\npython -m pytest weeks/week-13-modules-cli-api/checks\n```\n\nBộ `test_exercises.py` kiểm tra các file trong `exercises/`; `test_solutions.py`\nkiểm tra lời giải tham khảo trong `solutions/`. Hai bộ test không thay thế cho nhau.
