texto = input("Ingrese un texto: ")
suma = 0
suma2 = 0

for c in texto:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        suma += 1
    else:
        suma2 += 1

print("La cantidad de vocales es: ", suma)
print("La cantidad de consonantes es: ", suma)