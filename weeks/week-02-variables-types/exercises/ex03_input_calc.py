"""Bài tập 03: Máy tính nhận input 🖥️"""
# TODO 1: Nhập hai số và in tổng, hiệu, tích, thương
try:
    so_thu_nhat = float(input("Nhập số thứ nhất: "))
    so_thu_hai = float(input("Nhập số thứ hai: "))
    print("Tổng:", so_thu_nhat + so_thu_hai)
    print("Hiệu:", so_thu_nhat - so_thu_hai)
    print("Tích:", so_thu_nhat * so_thu_hai)
    if so_thu_hai == 0:
        print("Thương: Không thể chia cho 0.")
    else:
        print("Thương:", so_thu_nhat / so_thu_hai)
except ValueError:
    print("Vui lòng nhập hai giá trị hợp lệ dạng số.")

# TODO 2: Diện tích và chu vi hình tròn
try:
    pi = 3.14159
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    if ban_kinh < 0:
        print("Bán kính không được âm.")
    else:
        print(f"Diện tích: {pi * ban_kinh ** 2:.2f}")
        print(f"Chu vi: {2 * pi * ban_kinh:.2f}")
except ValueError:
    print("Vui lòng nhập bán kính hợp lệ dạng số.")

# TODO 3: Giá sau khi giảm
try:
    gia_goc = float(input("Nhập giá gốc (VNĐ): "))
    phan_tram_giam = float(input("Nhập phần trăm giảm giá: "))
    if gia_goc < 0 or not 0 <= phan_tram_giam <= 100:
        print("Giá gốc phải không âm và phần trăm giảm nằm trong khoảng 0–100.")
    else:
        gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
        print(f"Giá sau khi giảm: {gia_sau_giam:,.0f} VNĐ")
except ValueError:
    print("Vui lòng nhập giá và phần trăm giảm bằng số.")

# TODO 4: Đổi VNĐ sang USD theo tỷ giá nhập vào
try:
    tien_vnd = float(input("Nhập số tiền (VNĐ): "))
    ty_gia = float(input("Nhập tỷ giá (VNĐ cho 1 USD): "))
    if tien_vnd < 0 or ty_gia <= 0:
        print("Số tiền phải không âm và tỷ giá phải lớn hơn 0.")
    else:
        print(f"Số USD tương ứng: ${tien_vnd / ty_gia:.2f}")
except ValueError:
    print("Vui lòng nhập số tiền và tỷ giá hợp lệ.")
