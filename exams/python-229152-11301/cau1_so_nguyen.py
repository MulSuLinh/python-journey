"""Cau 1: Kiem tra n, dem chu so le va tinh tong phan so."""


def nhap_n():
    """Nhap so nguyen n trong khoang tu 1 den 1500."""
    while True:
        try:
            n = int(input("Nhap n (1..1500): "))
            if 1 <= n <= 1500:
                return n
            print("Gia tri khong hop le. Hay nhap lai!")
        except ValueError:
            print("Vui long nhap mot so nguyen.")


def dem_chu_so_le(n):
    """Dem so chu so le cua so nguyen duong n."""
    dem = 0
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 == 1:
            dem += 1
        n //= 10
    return dem


def tinh_tong(n):
    """Tinh S = 1/2 + 1/4 + ... + 1/(2*n)."""
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (2 * i)
    return tong


def main():
    n = nhap_n()
    print("So chu so le:", dem_chu_so_le(n))
    print("Tong S =", tinh_tong(n))


if __name__ == "__main__":
    main()
