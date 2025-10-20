# Câu 7: Tính và xuất độ dài đoạn AB
# Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. 

import math
def khoangcach(xA, yA, xB, yB):
    return math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))
print("Độ dài đoạn AB là:", khoangcach(xA, yA, xB, yB))
