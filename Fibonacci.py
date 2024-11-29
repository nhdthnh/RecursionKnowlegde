# Hàm Fibonacci không sử dụng memoization
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Hàm Fibonacci sử dụng memoization
memo = {}
def fibonacci_memoization(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
        return memo[n]
    
def fibonacci_iterative(n):
    if n <= 0:
        return 0  # Số Fibonacci thứ 0 là 0
    elif n == 1:
        return 1  # Số Fibonacci thứ 1 là 1
    a, b = 0, 1  # a = Fibonacci(0), b = Fibonacci(1)
    for i in range(2, n + 1):
        # Sử dụng một biến tạm thời để đảm bảo cập nhật đúng
        temp = b
        b = a + b
        a = temp  # Cập nhật `a` sau khi `b` đã được tính toán
    return b


# Kiểm tra với n = 10
n = 10
result_recursive = fibonacci_recursive(n)
result_memoization = fibonacci_memoization(n)
result_iterative = fibonacci_iterative(n)
print(f"Kết quả Fibonacci với n = {n}:")
print(f"1. Sử dụng đệ quy không memoization: {result_recursive}")
print(f"2. Sử dụng memoization: {result_memoization}")
print(f"3. Sử dụng phương pháp lặp: {result_iterative}")
