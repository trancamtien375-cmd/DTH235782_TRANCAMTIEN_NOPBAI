# Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
# đúng phép toán đã nhập.

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Lỗi: Không thể chia cho 0"
    else:
        return "Lỗi: Phép toán không hợp lệ"

# --- Chạy thử ---
a = float(input("Nhập vào giá trị a: "))
b = float(input("Nhập vào giá trị b: "))
operator = input("Nhập vào phép toán (+, -, *, /): ")

result = calculate(a, b, operator)
print(f"Kết quả: {result}")
# Ví dụ:
# Nhập vào giá trị a: 5
# Nhập vào giá trị b: 10
# Nhập vào phép toán (+, -, *, /): *