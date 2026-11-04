"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))
print("Tổng:", so_thu_nhat + so_thu_hai)
print("Hiệu:", so_thu_nhat - so_thu_hai)
print("Tích:", so_thu_nhat * so_thu_hai)
if so_thu_hai != 0:
    print("Thương:", so_thu_nhat / so_thu_hai)
else:
    print("Không thể tính thương vì số thứ hai bằng 0.")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Nhập bán kính hình tròn: "))
if ban_kinh >= 0:
    dien_tich = pi * ban_kinh ** 2
    chu_vi = 2 * pi * ban_kinh
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
else:
    print("Bán kính không được âm.")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc (VNĐ): "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá: "))
if gia_goc >= 0 and 0 <= phan_tram_giam <= 100:
    gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
    print(f"Giá sau khi giảm: {gia_sau_giam:,.0f} VNĐ")
else:
    print("Giá gốc phải không âm và phần trăm giảm phải từ 0 đến 100.")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền (VNĐ): "))
ty_gia = float(input("Nhập tỷ giá (VNĐ cho 1 USD): "))
if so_tien_vnd >= 0 and ty_gia > 0:
    so_tien_usd = so_tien_vnd / ty_gia
    print(f"Số tiền tương ứng: {so_tien_usd:.2f} USD")
else:
    print("Số tiền phải không âm và tỷ giá phải lớn hơn 0.")
