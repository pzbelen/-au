n = -1
while n < 0:
    n = int(input("Ingrese un valor "))
    
factorial = 1
suma = 0
for a in range (1,n+1):
    factorial *= a
    suma += factorial
    
print(suma)

