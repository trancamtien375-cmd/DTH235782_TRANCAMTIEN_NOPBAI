# Câu 19: Tính giá trị biểu thức S
# Yêu cầu:
# Nhập s(x,n) = x + x^3/3! + x^5/5! + ... + x^n/n!

x = int(input("Nhập x: "))
n = int(input("Nhập n (là số lẻ): "))   
S = 0
t = 1  # Biến t dùng để lưu giá trị x^i
gt = 1 # Biến gt dùng để lưu giá trị i!
for i in range(1, n + 1, 2): # i chạy từ 1 đến n, bước nhảy là 2 (chỉ lấy số lẻ)
    t = t * x * x  # Cập nhật giá trị x^i
    gt = gt * i * (i - 1) if i > 1 else 1  # Cập nhật giá trị i! (với i=1 thì gán gt=1)
    S += t / gt  # Cộng dồn vào S
print("Giá trị biểu thức S là:", S)
