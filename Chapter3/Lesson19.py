# Câu 19: Tính giá trị biểu thức S
# Yêu cầu:
# Nhập s(x,n) = x + x^3/3! + x^5/5! + ... + x^n/n!

x = int(input("Nhập x: "))
n = int(input("Nhập n (số lẻ): "))
S = 0
tich = 1  #biến lưu giai thừa
for i in range(1, n + 1, 2):
    tich = tich * i * (i - 1)  #tính giai thừa
    S = S + (x ** i) / tich #cộng dồn vào S
print("S = ", S)
# Chương trình tính giá trị biểu thức S theo yêu cầu

