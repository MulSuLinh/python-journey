"""Exercise 01 — Functions and return values.

Goal:
    Viết các hàm nhỏ và dùng ``return`` thay vì chỉ ``print``.

TODO:
    1. Hoàn thành ``chao``.
    2. Hoàn thành ``tinh_dien_tich_hinh_tron``.
    3. Hoàn thành ``la_so_chan``.
"""
import math


def chao(ten: str) -> str:
    """Trả về lời chào cho ``ten``."""
    return f"Xin chào {ten}!"


def tinh_dien_tich_hinh_tron(ban_kinh: float) -> float:
    """Trả về diện tích hình tròn."""
    if ban_kinh < 0:
        raise ValueError("Bán kính không được âm")
    return math.pi * ban_kinh ** 2


def la_so_chan(so: int) -> bool:
    """Trả về True khi ``so`` là số chẵn."""
    return so % 2 == 0


if __name__ == "__main__":
    print(chao("An"))
    print(f"Diện tích: {tinh_dien_tich_hinh_tron(2):.2f}")
    print(la_so_chan(4))
