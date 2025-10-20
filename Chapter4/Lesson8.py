# Câu 8: Viết chương trình tính loga

# Yêu cầu:
# Viết chương trình tính loga
# x với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
# != 1.( dùng logax=lnx/lna)

import math
a = float(input("Nhap a > 0, a != 1: "))
x = float(input("Nhap x > 0: "))
if a <= 0 or a == 1 or x <= 0:
    print("Gia tri a hoac x khong hop le")
else:
    loga_x = math.log(x) / math.log(a)
    print("log", a, "(", x, ") =", loga_x)

