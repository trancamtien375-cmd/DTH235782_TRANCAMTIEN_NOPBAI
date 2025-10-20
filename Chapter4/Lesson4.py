# Câu 4: Viết Hàm tính ROI

def ROI(dt, cp):
    return (dt - cp) / cp
def GoiYDauTu (roi):
    if roi >= 0.75:
        return "Nen dau tu"
    elif roi >= 0.5:
        return "Co the xem xet"
    elif roi >= 0.2:
        return "Nen can nhac"
    else:
        return "Khong nen dau tu"
    
print("Chuong trinh tinh ROI")
dt = int(input("Nhap doanh thu (VND): "))
cp = int(input("Nhap chi phi(VND): "))
roi = ROI(dt, cp)
print("Ti le ROI= ", roi)
print("==>", GoiYDauTu(roi))