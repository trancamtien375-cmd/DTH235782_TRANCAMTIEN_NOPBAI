# Câu 18: Vẽ các hình dưới đây
# Yêu cầu:
# Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây

n = int(input("Nhập chiều cao n: "))
print("___________________________\n")
# for i in range(1, n + 1):
#     print('*' * i)
# for i in range(n - 1, 0, -1):
#     print('*' * i)
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * i)


#Hình vuông rỗng
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('*' * n)
#     else:
#         print('*' + ' ' * (n - 2) + '*')

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()

print("___________________________\n")

#Hình tam giác cân lệch phải
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

print("___________________________\n")

#Hai hình tam giác cân rỗng
mid = n - 1   # dòng giữa (vị trí hàng ngang)

for i in range(n):
    for j in range(n):
        # phần 1: chéo từ (0,0) xuống (mid-1, mid-1)
        if i < mid and j == i:
            print("*", end=" ")
        # phần 2: hàng ngang giữa
        elif i == mid:
            print("*", end=" ")
        # phần 3: chéo từ (mid+1, mid+1) xuống (n-1, n-1)
        elif i > mid and j == n - 1 - (i - mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#Chương trình vẽ các hình theo yêu cầu
