# Tuần 15 — Capstone · Tests · README · Git/GitHub

Tuần cuối tích hợp kỹ năng đã học thành bằng chứng có thể chạy, đọc và review.

## Tài liệu tuần 15

- [Ôn lý thuyết Python thật đơn giản](theory-review.md): tóm tắt kiến thức tuần 1–15 bằng lời dễ nhớ.
- [Ví dụ capstone Expense Tracker](../../projects/expense-tracker-capstone/README.md): dự án tham khảo có code và test; hãy chạy, đọc và tự chỉnh sửa, không nộp nguyên trạng.
- [Integration checklist](notes.md) và [gợi ý theo hạng mục](hints.md).

## Canonical capstone

Đề bài, deliverables và rubric duy nhất nằm tại [FINAL_PROJECT.md](../../FINAL_PROJECT.md). Week 15 không định nghĩa rubric thứ hai và VuaCóc Bot không phải lựa chọn bắt buộc.

## Outcomes

- Hoàn thiện một vertical slice có phạm vi rõ.
- Chạy tests và ghi các giới hạn còn lại.
- Viết README có setup, usage, test, bằng chứng và limitations.
- Tạo commit history dễ review.
- Demo một kết quả có thể tái hiện.

Flagship optional track: [VuaCóc Bot Journey](../../projects/vuacoc-bot-journey/README.md), gồm local tournament và replay course-local.

Starter documentation:

- [Capstone README template](../../templates/capstone-readme-template.md)
- [AI usage template](../../templates/AI_USAGE.template.md)

## Readiness check

Week 15 không có bộ đáp án chính thức: deliverable chính là project của người học. Hãy tự kiểm tra evidence trước khi handoff:

~~~bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py projects/expense-tracker-capstone
~~~

Check xác nhận README có setup/usage/test, có AI_USAGE.md, đủ hàm, đủ test, pytest collect được và không có bare except. Nó không chấm điểm — rubric duy nhất vẫn nằm tại [FINAL_PROJECT.md](../../FINAL_PROJECT.md).

Chi tiết: [checks/README.md](checks/README.md).
