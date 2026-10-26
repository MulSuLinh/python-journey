# Week 14 — Lời giải tham khảo

Lời giải chính thức được gom trong oop_models.py để tránh lặp code giữa nhiều exercise.

- Progress: ví dụ class/object, __init__, method và __str__.
- Bot: ví dụ composition; strategy được truyền vào khi tạo bot.
- defensive, balanced, aggressive: ba strategy mẫu.
- Animal và Dog: ví dụ inheritance với quan hệ “Dog là một Animal”.

## Chạy và tự kiểm tra

~~~bash
python weeks/week-14-oop-essentials/checks/check_week.py
python -m pytest weeks/week-14-oop-essentials/checks/test_solutions.py
~~~

Lời giải nên được đọc sau khi thử làm exercises. Hãy kiểm tra strategy với mục tiêu ở cả hai hướng, rồi giải thích vì sao composition giúp đổi hành vi mà không sửa class Bot.
