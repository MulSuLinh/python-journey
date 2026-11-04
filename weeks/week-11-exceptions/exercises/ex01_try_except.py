"""Exercise 01: expected bad input."""

raw_turn = "not-a-number"

try:
    turn = int(raw_turn)
except ValueError:
    print(f"Giá trị lượt chơi không hợp lệ: {raw_turn!r} (cần một số nguyên).")
else:
    print(f"Turn: {turn}")
