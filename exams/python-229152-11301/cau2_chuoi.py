"""Cau 2: Xu ly chuoi."""


def dem_chu_hoa(s):
    """Dem so ky tu chu hoa trong chuoi."""
    dem = 0
    for ky_tu in s:
        if ky_tu.isupper():
            dem += 1
    return dem


def la_chuoi_doi_xung(s):
    """Tra ve True neu chuoi doc xuoi va nguoc giong nhau."""
    return s == s[::-1]


def tong_cac_chu_so(s):
    """Tinh tong cac ky tu la chu so trong chuoi."""
    tong = 0
    for ky_tu in s:
        if ky_tu.isdigit():
            tong += int(ky_tu)
    return tong


def main():
    s = input("Nhap chuoi s: ")

    print("So ky tu chu hoa:", dem_chu_hoa(s))

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Tong cac chu so trong chuoi:", tong_cac_chu_so(s))


if __name__ == "__main__":
    main()
