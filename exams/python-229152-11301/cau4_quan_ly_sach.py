"""Cau 4: Quan ly thong tin sach bang tu dien."""

from datetime import date


def nhap_sach():
    """Nhap danh sach sach va luu vao dictionary theo ma so."""
    tu_dien = {}

    while True:
        try:
            n = int(input("Nhap so luong sach (n > 0): "))
            if n > 0:
                break
            print("So luong phai lon hon 0.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    nam_hien_tai = date.today().year

    for i in range(n):
        print(f"\nNhap thong tin sach thu {i + 1}:")
        while True:
            ma_sach = input("Ma so sach: ").strip()
            if not ma_sach:
                print("Ma sach khong duoc de trong.")
            elif ma_sach in tu_dien:
                print("Ma sach da ton tai. Hay nhap ma khac.")
            else:
                break

        ten_sach = input("Ten sach: ").strip()
        ten_tac_gia = input("Ten tac gia: ").strip()
        nha_xuat_ban = input("Nha xuat ban: ").strip()

        while True:
            try:
                nam_xuat_ban = int(input("Nam xuat ban: "))
                if 0 < nam_xuat_ban <= nam_hien_tai:
                    break
                print(f"Nam xuat ban phai tu 1 den {nam_hien_tai}.")
            except ValueError:
                print("Nam xuat ban phai la so nguyen.")

        tu_dien[ma_sach] = {
            "TenSach": ten_sach,
            "TenTacGia": ten_tac_gia,
            "NhaXuatBan": nha_xuat_ban,
            "NamXuatBan": nam_xuat_ban,
        }

    return tu_dien


def xoa_sach(tu_dien, ma_sach):
    """Xoa sach theo ma; tra ve True neu tim thay."""
    if ma_sach in tu_dien:
        del tu_dien[ma_sach]
        return True
    return False


def main():
    tu_dien = nhap_sach()
    print("\nDanh sach sach:")
    for ma_sach, thong_tin in tu_dien.items():
        print(ma_sach, ":", thong_tin)

    ma_can_xoa = input("\nNhap ma sach can xoa: ").strip()
    if xoa_sach(tu_dien, ma_can_xoa):
        print(f"Cuon sach co ma {ma_can_xoa} da duoc xoa.")
    else:
        print("Khong tim thay cuon sach can xoa.")

    print("Tu dien sau khi xu ly:", tu_dien)


if __name__ == "__main__":
    main()
