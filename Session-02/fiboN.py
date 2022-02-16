def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n + 1):
            num = n1 + n2
            n1 = n2
            n2 = num  # never put a return inside a loop
        return num

print("5th Fibonacci´s term:", fib(5))
print("10th Fibonacci´s term:", fib(10))
print("15th Fibonacci´s term:", fib(15))


