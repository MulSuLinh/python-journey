"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
try:
    so_du = int(input("Số dư hiện tại (VND): "))
    so_tien_rut = int(input("Số tiền muốn rút (VND): "))
    if so_tien_rut <= 0:
        print("Số tiền rút phải lớn hơn 0.")
    else:
        if so_tien_rut % 50000 != 0:
            print("Số tiền rút phải là bội số của 50.000 VND.")
        elif so_tien_rut > so_du:
            print("Số dư không đủ.")
        else:
            so_du -= so_tien_rut
            print(f"Rút tiền thành công. Số dư còn lại: {so_du:,} VND")
except ValueError:
    print("Số dư và số tiền rút phải là số nguyên.")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
try:
    chieu_cao = float(input("\nChiều cao (m): "))
    can_nang = float(input("Cân nặng (kg): "))
    if chieu_cao <= 0 or can_nang <= 0:
        print("Chiều cao và cân nặng phải lớn hơn 0.")
    else:
        bmi = can_nang / (chieu_cao ** 2)
        print(f"Chỉ số BMI của bạn: {bmi:.1f}")
        if bmi < 18.5:
            print("Thiếu cân — bạn có thể cần tăng cân.")
        elif bmi < 25:
            print("Bình thường — hãy tiếp tục duy trì nhé!")
        elif bmi < 30:
            print("Thừa cân — hãy chú ý chế độ ăn và vận động.")
        else:
            print("Béo phì — nên trao đổi với bác sĩ để được tư vấn.")
except ValueError:
    print("Vui lòng nhập chiều cao và cân nặng hợp lệ.")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("\nLoại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
try:
    tuoi = int(input("Tuổi: "))
    if loai_ve not in ("thuong", "vip") or ngay not in ("thuong", "cuoi_tuan") or tuoi < 0:
        print("Thông tin vé hoặc tuổi không hợp lệ.")
    else:
        if loai_ve == "thuong":
            gia_ve = 80000
        else:
            gia_ve = 120000

        if ngay == "cuoi_tuan":
            gia_ve *= 1.3

        if tuoi < 12 or tuoi >= 65:
            gia_ve *= 0.5
        elif 18 <= tuoi <= 25:
            gia_ve *= 0.8

        print(f"Giá vé cuối cùng: {gia_ve:,.0f} VND")
except ValueError:
    print("Tuổi phải là số nguyên.")
