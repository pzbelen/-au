n = -1
while n < 0:
    n = int(input("Ingrese un valor "))
    
factorial = 1
for a in range (1,n+1):
    factorial *= a

print(factorial)