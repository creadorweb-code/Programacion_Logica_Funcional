###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)          # True
print("5 < 3:", 5 < 3)          # False
print("5 == 5:", 5 == 5)        # True (igualdad)
print("5 != 3:", 5 != 3)        # True (desigualdad)
print("5 >= 5:", 5 >= 5)        # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)        # False (menor o igual que)

print("\nComparación de cadenas:")
print('"manzana" < "pera":', "manzana" < "pera")   # True
print('"Hola" == "hola":', "Hola" == "hola")       # False

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("True or False:", True or False)     # True
print("False or False:", False or False)   # False
print("not True:", not True)               # False
print("not False:", not False)             # True

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A    B    A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\nor:")
print("A    B    A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:")
print("A    not A")
print("True ", not True)
print("False", not False)


###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]


print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3])  # [1, 2, 3]
print(lista1[3:])  # [4, 5]
print(lista1[:])   # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2])  # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))