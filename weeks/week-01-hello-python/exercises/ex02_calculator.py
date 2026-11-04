"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
tong = 2024 + 1000
print("2024 + 1000 =", tong)


# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
so_tien = 150_000
tien_ca_phe = 3 * 35_000
tien_con_lai = so_tien - tien_ca_phe
print("Số tiền còn lại:", tien_con_lai, "VNĐ")


# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
ban_kinh = 7
dien_tich = 3.14159 * ban_kinh ** 2
print("Diện tích hình tròn:", dien_tich)


# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
so_keo = 100
so_nguoi = 7
print("Mỗi người được:", so_keo // so_nguoi, "viên")
print("Số kẹo còn dư:", so_keo % so_nguoi, "viên")


# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
do_c = 37
do_f = do_c * 9 / 5 + 32
print(f"{do_c}°C = {do_f}°F")
