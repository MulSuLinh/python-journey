"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
try:
    tuoi = int(input("Tuổi: "))
    co_bang_lai = input("Có bằng lái? (y/n): ").strip().lower() == "y"
    khong_say = input("Tỉnh táo? (y/n): ").strip().lower() == "y"
    if tuoi >= 18 and co_bang_lai and khong_say:
        print("Bạn đủ điều kiện lái xe.")
    else:
        print("Bạn chưa đủ điều kiện lái xe.")
except ValueError:
    print("Tuổi phải là số nguyên.")

# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
try:
    a = float(input("\nNhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Tam giác đều.")
        elif a == b or a == c or b == c:
            print("Tam giác cân.")
        else:
            print("Tam giác thường.")
    else:
        print("Ba cạnh không tạo thành tam giác.")
except ValueError:
    print("Vui lòng nhập ba cạnh hợp lệ.")

# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
pw = input("\nNhập mật khẩu cần kiểm tra: ")
if (len(pw) >= 8 and any(c.isupper() for c in pw)
        and any(c.islower() for c in pw)
        and any(c.isdigit() for c in pw)):
    print("Mật khẩu mạnh.")
else:
    print("Mật khẩu chưa đủ mạnh (cần ít nhất 8 ký tự, chữ hoa, chữ thường và chữ số).")

# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
try:
    n = int(input("\nNhập số nguyên n: "))
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
except ValueError:
    print("Vui lòng nhập số nguyên.")
