
from os import system
if system("clear") !=0: system("cls")

"""
El comando 'type()' devuelve el tipo de un objeto en Python
"""

print("int:") # Enteros (numeros sin parte decimal0)
print(type(10)) # Numeros entero positivo
print(type(0)) # El numero cero tambien es un entero
print(type(-5)) # Numero entero negativo
print(type(12345677888099887654322)) # Python permite enteros de gran tamaño

print("float:") # numeros decimales (de punto flotante)
print(type(3.14)) # Numero con punto decimal
print(type(1.0)) # Tambien es considerado un float, aunque sea un numero con punto decimal
print(type(1e3)) # Notación cientifica (equivalente a 1000.0)

print("complex:") # numeros complejos (con parte real e imaginaria)
print(type(1+2j))# un numero complejo en python (1 es la parte real, 2j es la parte imaginaria)

print("str:") # Cadenas de texto (string)
print(type("Hola")) # Un string con texto
print(type("")) # Un string vacio
print(type("123")) # Aunque parezca un numero, esta entre comillas
print(type("""
           Multilinea
           """))

print("bool:") # Valores booleanos (True and False)
print(type(True))
print(type(False))
print(type(1<2))

print("NoneType:") # Representa la ausencia de valor
print(type(None)) # 'None' es un tipo especial en Python que representa "sin valor"
