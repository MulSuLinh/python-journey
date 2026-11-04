"""Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄"""
# TODO 1: Chuyển "42" sang int, cộng thêm 8
so_text = "42"
so_nguyen = int(so_text)
print("42 + 8 =", so_nguyen + 8)

# TODO 2: Chuyển pi sang int
pi = 3.14159
print("int(pi) =", int(pi))

# TODO 3: Kiểm tra bool() của các giá trị
gia_tri = [0, 1, "", "hello", [], [1, 2]]
for value in gia_tri:
    print(f"bool({value!r}) =", bool(value))

# TODO 4: Nhập chiều cao, cân nặng và tính BMI
try:
    chieu_cao = float(input("Nhập chiều cao (m): "))
    can_nang = float(input("Nhập cân nặng (kg): "))
    if chieu_cao <= 0 or can_nang <= 0:
        print("Chiều cao và cân nặng phải lớn hơn 0.")
    else:
        bmi = can_nang / chieu_cao ** 2
        print(f"BMI của bạn: {bmi:.1f}")
except ValueError:
    print("Vui lòng nhập chiều cao và cân nặng bằng số.")

# TODO 5: Đổi số giây thành giờ, phút, giây
try:
    tong_giay = int(input("Nhập số giây: "))
    if tong_giay < 0:
        print("Số giây không được âm.")
    else:
        gio = tong_giay // 3600
        phut = (tong_giay % 3600) // 60
        giay = tong_giay % 60
        print(f"{gio} giờ {phut} phút {giay} giây")
except ValueError:
    print("Vui lòng nhập số giây là số nguyên.")
