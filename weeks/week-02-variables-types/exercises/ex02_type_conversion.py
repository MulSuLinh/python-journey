"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# TODO 1: Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so_nguyen = int(so_text)
print("42 + 8 =", so_nguyen + 8)


# TODO 2: Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
print("int(pi) =", int(pi))


# TODO 3: Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
cac_gia_tri = [0, 1, "", "hello", [], [1, 2]]
for gia_tri in cac_gia_tri:
    print(f"bool({gia_tri!r}) =", bool(gia_tri))


# TODO 4: Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
if chieu_cao > 0 and can_nang >= 0:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"BMI của bạn: {bmi:.1f}")
else:
    print("Chiều cao phải lớn hơn 0 và cân nặng không được âm.")


# TODO 5 (Thử thách): Nhập số giây, chuyển sang giờ:phút:giây
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
tong_giay = int(input("Nhập số giây: "))
if tong_giay >= 0:
    gio = tong_giay // 3600
    phut = (tong_giay % 3600) // 60
    giay = tong_giay % 60
    print(f"{gio} giờ {phut} phút {giay} giây")
else:
    print("Số giây không được âm.")
