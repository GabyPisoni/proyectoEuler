# Multiplos de 3 y 5
""""Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000."""
print("Vamos a buscar todos los multiplos de 3 y 5 que esten debajo de 1000 y informar el total")


def multiplosX1000():
    total = 0
    lista = []
    for element in range(1000):
        # print(element)
        if(element % 3 == 0 or element % 5 == 0):
            total += element
            lista.append(element)

    return print("\nLa lista de elementos multiplos de 3 y 5 x debajo de 1000 es ", lista, "\nY la suma total es", total)


multiplosX1000()
