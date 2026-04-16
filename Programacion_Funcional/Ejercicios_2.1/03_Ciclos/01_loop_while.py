
from os import system

if system("clear") != 0: system("cls")

print("\n Blucle while:")

# Bucle con una simple condición

contador = 0

while contador <=5:  #valor que 
    print(contador)
    contador +=1

    #Utilizando la palabras break para romper en bluce

    print("\n Blucle while con break:")

    contador = 0

    while True:
        print(contador)
        contador = 1
        if contador == 5:
            break           # Sale del bucle


# continue, que lo hace es saltar esa iteracion en concreto
# y continuar con el bucle

        print("\n Bucle con continue")
        contador = 0
        while contador < 10:
            contador += 1

            if contador %2== 0:
                continue

            print(contador)
            
# else, esta condición cuando se ejecuta
            
print("\n Bucle while con else:") 
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminador")

 # pedirle al usuario un numero que tiene
# que ser positivo si no, no le dejams en paz   

numero = -1

while numero < 0:
    numero = int(input("Escribe un número positivo:"))
    if numero < 0:
        print("El número debe ser positivo. Intenta otra vez")

print(f"El número que has introducido es {numero}")

numero =-1

while numero <0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo, intenta otra vez")
    except:
        print("Lo que introduces debe ser un número")

print(f"El número que introdujiste es {numero}")

#gracias





