"""Cau 5: Tao lop DienThoai va hai doi tuong."""


class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        """Hien thi day du thong tin cua dien thoai."""
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin, "mAh")
        print("Gia ban:", format(self.GiaBan, ",").replace(",", "."), "dong")
        print("-" * 30)


def main():
    DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    DT01.thongtindienthoai()
    DT02.thongtindienthoai()


if __name__ == "__main__":
    main()
