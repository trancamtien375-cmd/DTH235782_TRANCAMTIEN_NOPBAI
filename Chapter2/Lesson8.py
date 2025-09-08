'''
1. Các loại lỗi khi lập trình Python
a) Lỗi cú pháp (Syntax Error)
Xảy ra khi code vi phạm cú pháp Python.

Trình thông dịch sẽ báo lỗi ngay khi chạy.

b) Lỗi thời gian chạy (Runtime Error / Exception)
Code viết đúng cú pháp nhưng gặp sự cố khi chạy.

Thường là do dữ liệu, chia cho 0, truy cập phần tử không tồn tại,…

c) Lỗi logic (Logic Error)
Chương trình chạy không báo lỗi, nhưng kết quả sai với mong đợi.

Khó phát hiện nhất vì Python không cảnh báo.

2. Cách bắt lỗi trong Python
Python dùng câu lệnh try ... except để xử lý ngoại lệ (Exception Handling).

a) Cú pháp cơ bản
try:
    # đoạn code có thể gây lỗi
    x = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
b) Bắt nhiều loại lỗi
try:
    a, b = map(int, input("Nhập 2 số: ").split())
    print(a / b)
except ValueError:
    print("Lỗi: nhập sai kiểu dữ liệu!")
except ZeroDivisionError:
    print("Lỗi: không thể chia cho 0!")
c) Dùng finally
finally luôn chạy dù có lỗi hay không (thường dùng để giải phóng tài nguyên).

try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Không tìm thấy file!")
finally:
    print("Kết thúc chương trình.")
'''