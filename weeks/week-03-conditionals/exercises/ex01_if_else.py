"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"
try:
    tuoi = int(input("Nhập tuổi: "))
    if tuoi < 0:
        print("Tuổi không hợp lệ.")
    elif tuoi < 13:
        print("Thiếu nhi")
    elif tuoi <= 17:
        print("Thiếu niên")
    elif tuoi <= 64:
        print("Người lớn")
    else:
        print("Người cao tuổi")
except ValueError:
    print("Vui lòng nhập tuổi bằng số nguyên.")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
try:
    diem = float(input("\nNhập điểm (0-10): "))
    if not 0 <= diem <= 10:
        print("Điểm không hợp lệ.")
    elif diem >= 9:
        print("Xếp loại: Xuất sắc")
    elif diem >= 8:
        print("Xếp loại: Giỏi")
    elif diem >= 6.5:
        print("Xếp loại: Khá")
    elif diem >= 5:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")
except ValueError:
    print("Vui lòng nhập điểm hợp lệ.")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
try:
    nam = int(input("\nNhập năm: "))
    if nam <= 0:
        print("Năm không hợp lệ.")
    elif nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        print(f"{nam} là năm nhuận.")
    else:
        print(f"{nam} không phải năm nhuận.")
except ValueError:
    print("Vui lòng nhập năm bằng số nguyên.")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
try:
    a = float(input("\nNhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    c = float(input("Nhập số thứ ba: "))
    if a >= b and a >= c:
        so_lon_nhat = a
    elif b >= a and b >= c:
        so_lon_nhat = b
    else:
        so_lon_nhat = c
    print("Số lớn nhất là:", so_lon_nhat)
except ValueError:
    print("Vui lòng nhập ba số hợp lệ.")
