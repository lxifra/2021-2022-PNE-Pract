
def fibosum(n):
    sum_n = 0
    for i in range(0, n+1):
        sum_n += i
    return sum_n

exit = False
count = 0
while not exit and count < 2:
    n = int(input("Insert a number: "))
    final_sum = fibosum(n)
    print("Sum of the ", n, "th term of the Fibonacci series: ", final_sum)
    count += 1