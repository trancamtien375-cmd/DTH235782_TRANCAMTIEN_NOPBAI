# Câu 11: Kiểm tra số nguyên tố
# Yêu cầu:
# Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
# hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.

while True:
    n=int(input("Nhập 1 số nguyên dương"))
    dem=0
    for i in range(1,n+1):
        if n % i ==0 :
            dem+=1
    if dem==2:
        print(n,"Là số nguyên tố")
    else:
        print(n,"Không là số nguyên tố")
    hoi=input("Tiếp không Thím?(c/k):")
    if hoi is "k":
        break
print("BYE!")

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# while True:
#     try:
#         number = int(input("Nhập một số nguyên (hoặc nhập 'thoát' để kết thúc): "))
#         if is_prime(number):
#             print(f"{number} là số nguyên tố.")
#         else:
#             print(f"{number} không phải là số nguyên tố.")
#     except ValueError:
#         print("Kết thúc chương trình.")
#         break
#     result = calculate(a, b, operator)
# print(f"Kết quả: {result}")
