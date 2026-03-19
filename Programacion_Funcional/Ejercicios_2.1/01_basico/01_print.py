

     
from os import system

#System() nos permite ejecutar un comando en la terminal
# En este caso, lo hacemos para limpiar la pantalla en MacOS\Linux usando "Clear" como en windows con "cls"
if system ("clear") != 0: system("cls")

# Este ejemplo basico de como imprimir un texto en consola
print("Hola, Crayola")

# Tambien puedes usar comillas simples para imprimir texto
print('Esto tambien funciona con una comilla')

# Puedes imprimir múltiples elementos separados por un espacio
print("Python", "es", "Genial")

# El parametro 'sep' permite definir como se separan los elementos impresos
print("Python", "es", "brutal", sep="-")

# El parametro 'end' define lo que se imprime al final de la linea 
print("Esto se imprime", end="\n") # Aqui, el 'end' tiene un salto de la linea esplicita
print("en una linea") # Esto se imprime en la linea seguiente

#Tambien se pueden imprimir numeros directamente
print(42)

# Ejemplo de como imprimir el simbolo de pulgadas (")
# Si usas comillas dobless dentro de un string con comillas dobles, se produce un error
# Print("Esto es una "pulgada") # X Esto generaria un error de sintaxis

# Bien Solución 1: Usar comillas simples para encerrar la cadena
print('Esto es una "pulgada" dentro de un string con comillas simples')

# Bien Solución 2: Usar el carácter de escape \ para incluir comillas dobles dentro de un string
print("Esto es una \"pulgada\" dentro de un string con comillas dobles")

# Bien Solucion 3: 
print("Esto es una \"pulgada\" dentro de un string con comillas triples")
# Esto es una "pulgada" dentro de un string con triples comillas