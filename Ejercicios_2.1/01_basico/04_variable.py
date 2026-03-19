from os import system
if system("clear") !=0: system("cls")

# Para asignarle una sola variables solo falta poner el nombre de la variable y asignarle un valor
my_name = "Carlos"
print(my_name) # Imprime ek valor de la variable my_name

age = 22
print(age) # Imprime el valor de la variable age

# Reasignar un nuevo valor
age = 24
print(age) # ahora se imprime el nuevo valor

# Tipado dinamico: el tipo de dato se determine en tiempo de ejecución
# No es necesario declarar explicitamente el tipo de variable

name = "Carlos"
print(type(name)) # muestra el tipo de dato de la variable name (str)

name = 32
print(type(name)) # ahora la variable tiene un numero entero (int)


# Tipado fuerte: python no realiza conversiones de tipo automaticas
# Esto genera un error porque no se puede sumar con una cadena
#print(10 + "2") # TypeError: unsupported operand type(s)

#f-string (literal de cadena de formato)
# desde la version python 3.6
print(f"Hola {my_name}, tengo{age + 5} años")

# No recomendada forma de asignar variables
name, age, city = "Carlos", 22, "FCP"

#convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

miNombreDeVariable = "no-recomdado" # camelCase
MiNombreDeVariable = "no-recomendado" # PascalCase
minombredevariable = "no-recomendado" # todo junto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 #UPPER_CASE -> constantes

# Anotaciones de tipo (opcional, para mayor claridad en el codigo)
is_user_loggend_in:bool = True # Indica que la variables es un booleno
print(is_user_loggend_in)

name: str = "Carlos" # indica
print(name)
