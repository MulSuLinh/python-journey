"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin học")
subjects.insert(1, "Lịch sử")
print("Sau append/insert:", subjects)
print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])

# TODO: update the first subject.
subjects[0] = "Toán nâng cao"
print("Sau cập nhật:", subjects)
print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])

# TODO: remove one known subject and pop the last subject.
if "Anh" in subjects:
    subjects.remove("Anh")
print("Sau remove:", subjects)
if subjects:
    removed = subjects.pop()
    print("Đã pop:", removed)
print("Danh sách cuối:", subjects)
if subjects:
    print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])

print(subjects)
