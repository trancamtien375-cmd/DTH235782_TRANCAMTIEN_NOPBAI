# Câu 1: Viết hàm để Tính diện tích tam giác
# Yêu cầu:
# Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác, Sau đó tính diện tích
# theo công thức Herong:

from math import sqrt
print("Chuong trinh tinh dien tich tam giac")
a = float(input("Nhap canh a > 0: "))
b = float(input("Nhap canh b > 0: "))
c = float(input("Nhap canh c > 0: "))

if ( a<=0 or b<=0 or c<=0) or (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print("Khong phai tam giac")
else:
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac la: ",s)
