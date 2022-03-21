#for i in range(1,21):
    #print(i, end=" ")

###       Sum the 20 first integers:
#sum = 0
#for i in range(1,21):
    #sum += i
    #print(sum, end=" ")
#print("\nTotal sum: ", sum)

###       Para que sea la suma de las integrales de el numero que tu quieras:
def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res
print("Sum of the 20 first integers: ", sumn(20))
print("Sum of the 100, frist integers: ", sumn(100))