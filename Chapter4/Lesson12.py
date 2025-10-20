# Câu 12: Hàm oscillate
# Yêu cầu:
# Cho mã lệnh:
# Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
# -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4

def oscillate(n):
    # Viết hàm ở đây
    # -3 3 -2 2 -1 1 0 0
    for i in range(n-1, 0, -1):
        print(-i, i, end=" ")
    print("0 0", end=" ")
    for i in range(n):
        print((i+1), -(i+1), end=" ")
    print()
oscillate(4)
