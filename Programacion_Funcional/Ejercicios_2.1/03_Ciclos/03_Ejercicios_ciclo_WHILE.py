from os import system

if system("clear") != 0: system("cls")

print("\n### EJERCICIOS (while) ###\n")

# Ejercicio 1: Cuenta atrás

print("Ejercicio 1: Cuenta atrás")

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares

print("\nEjercicio 2: Suma de números pares entre 1 y 20")

suma = 0
numero = 1
while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de los números pares entre 1 y 20 es: {suma}")


# Ejercicio 3: Factorial de un número

print("\nEjercicio 3: Factorial de un número")

numero = -1
while numero <= 0:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero <= 0:
            print("El número debe ser positivo. Intenta otra vez.")
    except:
        print("Lo que introduces debe ser un número entero.")

factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1

print(f"El factorial de {numero} es: {factorial}")


# Ejercicio 4: Validación de contraseña

print("\nEjercicio 4: Validación de contraseña")

contrasena = ""
while len(contrasena) < 8:
    contrasena = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Intenta otra vez.")

print("Contraseña válida")


# Ejercicio 5: Tabla de multiplicar

print("\nEjercicio 5: Tabla de multiplicar")

numero = -1
while numero <= 0:
    try:
        numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
        if numero <= 0:
            print("El número debe ser positivo. Intenta otra vez.")
    except:
        print("Lo que introduces debe ser un número entero.")

print(f"\nTabla de multiplicar del {numero}:")
multiplicador = 1
while multiplicador <= 10:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1


# Ejercicio 6: Números primos hasta N

print("\nEjercicio 6: Números primos hasta N")

n = -1
while n <= 0:
    try:
        n = int(input("Introduce un número entero positivo N: "))
        if n <= 0:
            print("El número debe ser positivo. Intenta otra vez.")
    except:
        print("Lo que introduces debe ser un número entero.")

print(f"\nNúmeros primos menores o iguales que {n}:")

numero = 2
while numero <= n:
    es_primo = True
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)
    numero += 1