# Câu 18: Vẽ các hình dưới đây
# Yêu cầu:
# Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây

n = 4
print("___________________________\n")

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()

print("___________________________\n")

#Hình tam giác vuông cân lệch phải
for i in range(n):
    for j in range(n):
        # In sao khi cột >= hàng (để canh phải)
        if j >= n - 1 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("___________________________\n")


#hình tam giác vuông rỗng

for i in range(n*2-1):
    for j in range(n*2 - 1):
        # Cột trái luôn có *
        if j == 0 and i < n - 1 or j == n*2 - 2 and i >= n - 1:
            print("*", end=" ")
        # Đường chéo chính
        elif j == i:
            print("*", end=" ")
        # Hàng cuối in toàn *
        elif i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


