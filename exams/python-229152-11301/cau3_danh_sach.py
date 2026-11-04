"""Cau 3: Nhap va xu ly danh sach so nguyen."""


def nhap_danh_sach():
    """Nhap cac so nguyen; nhap 0 de ket thuc."""
    danh_sach = []
    while True:
        try:
            x = int(input("Nhap so nguyen (0 de dung): "))
            if x == 0:
                break
            danh_sach.append(x)
        except ValueError:
            print("Du lieu khong hop le. Hay nhap so nguyen.")
    return danh_sach


def tong_so_duong_chan(danh_sach):
    """Tinh tong cac so duong va chan."""
    tong = 0
    for x in danh_sach:
        if x > 0 and x % 2 == 0:
            tong += x
    return tong


def dem_so_lan_xuat_hien(danh_sach, k):
    """Dem so lan k xuat hien trong danh sach."""
    dem = 0
    for x in danh_sach:
        if x == k:
            dem += 1
    return dem


def main():
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)
    print("Tong cac so duong chan:", tong_so_duong_chan(danh_sach))

    try:
        k = int(input("Nhap gia tri k can dem: "))
        print(f"So lan {k} xuat hien:", dem_so_lan_xuat_hien(danh_sach, k))
    except ValueError:
        print("k phai la mot so nguyen.")


if __name__ == "__main__":
    main()
