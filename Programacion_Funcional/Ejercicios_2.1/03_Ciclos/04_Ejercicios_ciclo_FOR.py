from os import system

if system("clear") != 0: system("cls")

print("\n### EJERCICIOS (for) ###\n")


# Ejercicio 1: Imprimir números pares

print("Ejercicio 1: Números pares del 2 al 20")

for numero in range(2, 21):
    if numero % 2 == 0:
        print(numero)

# Con list comprehension 
pares = [num for num in range(2, 21) if num % 2 == 0]
print(f"Con list comprehension: {pares}")


# Ejercicio 2: Calcular la media de una lista

print("\nEjercicio 2: Media de una lista")

numeros = [10, 20, 30, 40, 50]
suma = 0

for numero in numeros:
    suma += numero

media = suma / len(numeros)
print(f"La lista es: {numeros}")
print(f"La media es: {media}")


# Ejercicio 3: Buscar el máximo de una lista

print("\nEjercicio 3: Número máximo de una lista")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]  # Tomamos el primero como referencia

for numero in numeros:
    if numero > maximo:
        maximo = numero

print(f"La lista es: {numeros}")
print(f"El número máximo es: {maximo}")


# Ejercicio 4: Filtrar cadenas por longitud

print("\nEjercicio 4: Palabras con más de 5 letras")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

# Con bucle for
palabras_largas = []
for palabra in palabras:
    if len(palabra) > 5:
        palabras_largas.append(palabra)

print(f"Lista original: {palabras}")
print(f"Con bucle for: {palabras_largas}")

# Con list comprehension
palabras_largas_comp = [palabra for palabra in palabras if len(palabra) > 5]
print(f"Con list comprehension: {palabras_largas_comp}")


# Ejercicio 5: Contar palabras que empiezan con una letra

print("\nEjercicio 5: Contar palabras que empiezan con una letra")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

letra = input("Introduce una letra: ").lower()

contador = 0
for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1

print(f"Palabras que empiezan con '{letra}': {contador}")

# Con enumerate para mostrar cuáles son
print(f"Las palabras que empiezan con '{letra}' son:")
for idx, palabra in enumerate(palabras):
    if palabra.startswith(letra):
        print(f"  índice {idx} → {palabra}")