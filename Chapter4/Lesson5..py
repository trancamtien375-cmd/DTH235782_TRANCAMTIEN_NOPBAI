# Câu 5: Viết hàm đệ qui Fibonacci

def fibonacci (n):
    if n<=2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def listfibo(n):
    for i in range (1, n+1):
        print(fibonacci(i), end=" ")

print(fibonacci(9))

listfibo(9)