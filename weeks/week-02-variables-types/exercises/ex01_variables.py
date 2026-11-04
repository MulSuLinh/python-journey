"""Bài tập 01: Biến trong Python 📦"""
# TODO 1: Khai báo 4 biến và in giá trị cùng kiểu dữ liệu
ten = "Python Learner"  # Thay bằng tên của bạn nếu muốn
tuoi = 18
diem_tb = 8.5
dang_hoc = True
print("ten =", ten, "- kiểu dữ liệu:", type(ten))
print("tuoi =", tuoi, "- kiểu dữ liệu:", type(tuoi))
print("diem_tb =", diem_tb, "- kiểu dữ liệu:", type(diem_tb))
print("dang_hoc =", dang_hoc, "- kiểu dữ liệu:", type(dang_hoc))

# TODO 2: Hoán đổi không dùng biến tạm
a = 10
b = 20
a, b = b, a
print("Sau khi hoán đổi: a =", a, ", b =", b)

# TODO 3: Augmented assignment
x = 100
x += 20
print("Sau += 20:", x)
x -= 10
print("Sau -= 10:", x)
x *= 2
print("Sau *= 2:", x)
x //= 3
print("Sau //= 3:", x)

# TODO 4: Multiple assignment
ho, ten_rieng, tuoi_nguoi = "Nguyen", "An", 18
print(f"Họ tên: {ho} {ten_rieng}, {tuoi_nguoi} tuổi")
