"""Exercise 03 — Local scope and avoiding unnecessary global state."""


def them_ghi_chu(danh_sach: list[str], noi_dung: str) -> bool:
    """Thêm ghi chú hợp lệ và báo thao tác có thành công hay không."""
    noi_dung = noi_dung.strip()
    if not noi_dung:
        return False
    danh_sach.append(noi_dung)
    return True


def tim_ghi_chu(danh_sach: list[str], tu_khoa: str) -> list[str]:
    """Trả về các ghi chú chứa từ khóa, không phân biệt hoa thường."""
    tu_khoa = tu_khoa.strip().casefold()
    return [ghi_chu for ghi_chu in danh_sach if tu_khoa in ghi_chu.casefold()]


def dem_ghi_chu(danh_sach: list[str]) -> int:
    """Trả về số ghi chú trong list được truyền vào."""
    return len(danh_sach)


if __name__ == "__main__":
    notes: list[str] = []
    them_ghi_chu(notes, "Học return")
    them_ghi_chu(notes, "Luyện Python")
    print(tim_ghi_chu(notes, "PYTHON"))
    print(dem_ghi_chu(notes))
