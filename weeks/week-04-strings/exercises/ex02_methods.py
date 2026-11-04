"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
print("Email:", email.strip().lower())

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
print("Title case:", sentence.title())
print("Số chữ o:", sentence.count("o"))
print("Thay thế:", sentence.replace("python", "PYTHON"))

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
full_name = input("Nhập họ tên đầy đủ: ").strip()
name_parts = full_name.split()
if name_parts:
    print("Họ:", name_parts[0])
    print("Tên:", name_parts[-1])
else:
    print("Bạn chưa nhập họ tên.")

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
filename = input("Nhập tên file: ").strip()
print("Tên file hợp lệ:", filename.lower().endswith((".py", ".txt", ".csv")))

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
message = input("Nhập chuỗi cần mã hóa Caesar: ")
try:
    shift = int(input("Nhập số bước dịch: ")) % 26
    encrypted = []
    for char in message:
        if "a" <= char <= "z":
            encrypted.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            encrypted.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            encrypted.append(char)
    print("Chuỗi đã mã hóa:", "".join(encrypted))
except ValueError:
    print("Số bước dịch phải là số nguyên.")
