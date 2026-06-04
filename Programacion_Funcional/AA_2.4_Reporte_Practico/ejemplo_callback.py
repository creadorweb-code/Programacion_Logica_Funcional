#primer orden
def operar(n1, n2, funcion);
    return funcion(n1, n2)

def suma(a, b);
    return a + b
  
def resta(a, b);  #funcion de primer orden
    return a-b

resultado = operar (5, 3,  suma)

ejecutarse en operar

print(resultado)

#primera clase


def saludo();
    return "Hola!"  #

mi_variable = saludo()  

def saludo2();
    return "Que tal!"

mi_variable2 = saludo2
print(mi_variable2())

#funcion de orden sperior

def elejir_operacion(operacion):
    def multiplicar(X):
        return x * 2
    def dividir(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicar
    else:
    return dividir

doble = elegir_operacion("multiplicar")
print(doble(10))

divide2 = elegir_operacion("dividir")
prin("divide2(10)")



#funcion lambda

doble = lambda x: x * 2
doble
print(doble(5))

def cuadrado(x):
    return x ** 2
print(cuadrado(4))


def aplicar_funcion(funcion, valor):
    return funcion(valor)
resultado = aplicar_funcion(3)

resultado = aplicar_funcion (lambda x: x ** 2, 4)






lista_saludos = list(map(saludar, alumnos))

#print(lista_saludos)


#compresion de listas en pyton

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

doble  =[]

for m in numero:
    doble.append(n*2)
    print(doble)

cuadrado = [num ** 2 for num in numeros]    

lista_cuadruple=list(map(lambda x: x*4, numeros))
print(lista_cuadruple)

cubo = [elemento ** 3 for elemento in numeros[]]


cadena = ["hola "+" que haces" for _ in range(3)]

