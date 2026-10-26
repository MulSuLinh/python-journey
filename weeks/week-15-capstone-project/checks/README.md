# Week 15 capstone readiness check

Machine check tự kiểm tra **submission của chính bạn** trước khi handoff. Nó xác
nhận evidence cơ học: README có setup/usage/test, có `AI_USAGE.md`, Python files
parse được, đủ hàm, có ít nhất 5 test, pytest collect được trong 30 giây và
không có bare `except:`. Check chỉ collect test, không thực thi toàn bộ test.

Check **không chấm điểm**. Rubric duy nhất nằm tại
[FINAL_PROJECT.md](../../../FINAL_PROJECT.md).

Chạy từ repository root, trỏ tới thư mục capstone của bạn:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

Kết quả thành công:

```text
Week 15 capstone readiness: PASS
```

Khi FAIL, mỗi dòng là một hạng mục cần sửa. Sửa xong chạy lại cho tới khi PASS,
rồi mới tới bước demo và review.
