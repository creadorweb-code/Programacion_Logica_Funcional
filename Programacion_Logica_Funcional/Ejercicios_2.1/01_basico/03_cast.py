###
# 03-casting de types
# Transformar un tipo de un valor a otro
###

from os import system
if system("clear") !=0: system("cls")

print("Conversión de tipos")

# Convertir una cadena que contiene un numero a un entero y sumarlo con otro entero
print(2 + int("100")) # Convierte "100" a un entero y suma2. Resultado: 102

# Convertir un entero a cadena para concatenar con otra cadena
print("100" + str(2)) # Convierte el numero 2 a cadena y lo concatena. Resultado: "1002"

# Convertir una cadena con un numero decimal a tipo float
print(type(float("3.1416"))) # Convierte "3.1416" a float y muestra su tipo. Resultado

# Convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416)) # Convierte 3.1416 a 3 eliminado la parte de decimal. Resultado 


# Evaluar valores numericos como booleanos
print(bool(3)) # Culaquier numero distinto de 0 es True. Resultado. True
print(bool(0)) # 0 es False. Resultado: False
print(bool(-1)) # Números negativos tambien son True. Resultado: True

#Evaluar cadenas cibmo booleanos
print(bool("")) # Una cadena vacia es False
print(bool(" ")) # Una cadena con espacios es True
print(bool("False")) # Una cadena con texto, aunque sea False es True

# Redondear un numero decimal
print(round(2.51)) # Redondea 2.51 al entero mas cercano. Resultado: 3



