"""
Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm).
"""

def doc_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn",
              "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        # Số có 1 chữ số
        return chu_so[n]

    chuc = n // 10
    donvi = n % 10

    # Hàng chục
    if chuc == 1:
        phan_chuc = "mười"
    else:
        phan_chuc = chu_so[chuc] + " mươi"

    # Hàng đơn vị
    if donvi == 0:
        phan_donvi = ""
    elif donvi == 1 and chuc > 1:
        phan_donvi = " mốt"
    elif donvi == 5 and chuc > 0:
        phan_donvi = " lăm"
    else:
        phan_donvi = " " + chu_so[donvi]

    return phan_chuc + phan_donvi

# --- Chạy thử ---
n = int(input("Nhập số (0–99): "))
if 0 <= n <= 99:
    print(doc_so(n).strip().capitalize())
else:
    print("Vui lòng nhập số từ 0 đến 99.")
