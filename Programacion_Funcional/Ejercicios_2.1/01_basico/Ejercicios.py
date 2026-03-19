from os import system

if system("clear") != 0: system ("cls")

####EJERCICIO 1 #####

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# Completa aquí
print("Hugo Sanchez")
print("Felipe Carrillo Puerto")


####EJERCICIO 2 ###
print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

###EJERCICIO 3####
print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")
##el floptante 3.99 queda en 3 ya que  int() corta los decimales
##(no redondea)###

# Completa aquí
cadena = "12345"

# Convertir a entero
entero = int(cadena)

# Convertir a float
flotante = float(entero)

# Convertir 3.99 a entero
numero = 3.99
entero2 = int(numero)

print("Entero:", entero, type(entero))
print("Float:", flotante, type(flotante))
print("3.99 a entero:", entero2, type(entero2))

###EJERCICIO 4#####
print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

### Completa aquí

nombre = "Hugo"
edad = 30
altura = 1.72

print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

##EJERCICIO 5####
print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí

import math

pi = math.p

redondeado = round(pi)


redondeado = round(pi / 2) 
resultado = redondeado / 2
  
print("Resultado:", resultado)


