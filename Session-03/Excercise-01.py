#representar las once primeras combinaciones de la lista de Fibonacci.
N = 11
n1 = 0
n2 = 1
#luego cambiar el valor de las dos variables
#usar el for loop
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, N): #tienes que poner dos porq ya imprimimos arriba dos números, entonces nos salen
    #debajo trece números en vez de once, que son los que queremos.
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print() #Esto es para printear un end of line character.