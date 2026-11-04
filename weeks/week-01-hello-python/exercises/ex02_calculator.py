"""Bài tập 02: Máy tính Python 🧮"""
# TODO 1: Tính và in 2024 + 1000
print("2024 + 1000 =", 2024 + 1000)

# TODO 2: Tiền còn lại sau khi mua 3 ly cà phê
tien_ban_dau = 150_000
so_ly_ca_phe = 3
gia_moi_ly = 35_000
tien_con_lai = tien_ban_dau - so_ly_ca_phe * gia_moi_ly
print("Tiền còn lại:", f"{tien_con_lai:,} VNĐ")

# TODO 3: Diện tích hình tròn bán kính 7
ban_kinh = 7
dien_tich = 3.14159 * ban_kinh ** 2
print("Diện tích hình tròn:", dien_tich)

# TODO 4: Chia 100 viên kẹo cho 7 người
so_keo = 100
so_nguoi = 7
print("Mỗi người được:", so_keo // so_nguoi, "viên kẹo")
print("Số kẹo còn dư:", so_keo % so_nguoi, "viên")

# TODO 5: Đổi 37 độ C sang Fahrenheit
do_c = 37
do_f = do_c * 9 / 5 + 32
print(f"{do_c}°C = {do_f:.1f}°F")
