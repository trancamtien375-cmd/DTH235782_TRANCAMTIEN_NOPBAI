# Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

def find_quarter(month):
    if month in (1, 2, 3):
        return "Quý 1"
    elif month in (4, 5, 6):
        return "Quý 2"
    elif month in (7, 8, 9):
        return "Quý 3"
    elif month in (10, 11, 12):
        return "Quý 4"
    else:
        return "Tháng không hợp lệ"

# --- Chạy thử ---
month = int(input("Nhập vào tháng: "))
quarter = find_quarter(month)
print(f"Tháng {month} thuộc {quarter}")
