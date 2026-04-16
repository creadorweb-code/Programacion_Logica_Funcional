from os import system

if system("clear") != 0: system("cls")

print("\n Blucle for:")

#Itera sobres una lista de frutas

frutas = ["manzanas", "pera","mandarina"]
for fruta in frutas:
    print(fruta)

#Itera sobre un rango iterable 

    cadena = "estudiante"
    for caracter in cadena:
        print(caracter)

#enumerate (())


frutas = ["manzanas", "pera","mandarina"]
for idx, value in enumerate(fruta):
    print(f"El índice es{idx} y la fruta es {value}")

#bucle anidados

letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


#break

print("\n break")

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro está escondido en el índice {idx}")
        break

#continue

print("\ncontinue")

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for idx, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

#comprension de listas

animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

#muestra los numeros pares de una lista

pares = [num for num in [1, 2, 3, 4, 5, 6,] if num % 2== 0]
print(pares)



     