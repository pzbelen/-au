n = int(input("Ingrese un valor"))
dividendo = n
cuociente = 0
resto = 0

while dividendo !=0:
    cuociente = dividendo//2
    resto = dividendo%2
    dividendo = cuociente
    print(cuociente)