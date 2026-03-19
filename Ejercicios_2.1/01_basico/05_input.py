from os import system

if system("clear") != 0: system ("cls")

nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola{nombre}, encantado de conocerte")

age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener múltiple valores a la vez")
contry, city = input("¿En qué país y cuidad vives?\n").split()

print(f"Vives en {contry}, {city}")


