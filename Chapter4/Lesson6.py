# Câu 6: Những giá trị nào có thể xuất hiện trong randrange(0, 100)
# Yêu cầu:
# Những giá trị nào có thể xuất hiện khi chạy randrange(0, 100)?
# 4.5 , 34 , -1, 100, 0, 99

from random import randrange
print("Cac gia tri co the xuat hien trong randrange(0, 100) la:")
for i in range(10):
    print(randrange(0, 100), end=" ")
# Cac gia tri co the xuat hien la: 0, 1, 2, ..., 98, 99

