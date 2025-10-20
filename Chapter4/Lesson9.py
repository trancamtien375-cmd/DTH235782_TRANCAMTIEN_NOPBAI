# Câu 9: Viết chương trình tính căn bậc 2 lồng nhau

# Tính s(n) = √(2 + √(2 + √(2 + ... + √(2)))) 

import math
def tinh_can_bac_2_long_nhau(n):
    if n == 1:
        return 1
    else:
        return math.sqrt(2 + tinh_can_bac_2_long_nhau(n - 1))

n = int(input("Nhập n: "))
print("s(", n, ") =", tinh_can_bac_2_long_nhau(n))
