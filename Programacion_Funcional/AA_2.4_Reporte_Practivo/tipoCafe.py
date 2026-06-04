#crea una funcion preparar cafe que no recibe parametros y devuelve una cadena que represente un taza de cafe americano

def preparar_cafe():
    return "cafe americano"

# crea otra funcion esta funcion devuelve una cadena que representa una taza de cafe de olla

def preparar_cafe_de_olla():
    return "cafe de olla"

#crea otra funcion ordenar cafe que acepte dos parametroas: una funcion que prepara cafe y numero de tazas

def ordenar_cafe(funcion_preparar_cafe, numero_tazas);
    tazas_cafe =[funcion_preparar_cafe() for _ in range(numoro_tazas))]
    return tazas_cafe

#dentro de la funcion ordenar crea una listaa que guarde las tazas de cafe



#dentro de la funcion ordenar. aplica la iteracion atravez de la lista por comprension para llamar a la funcion preprar_cafe segun el numero_tazas proporcionada

cafe_grupo_a = ordenar_cafe(preparar_cafe_americano, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_de_olla, 12)

print(cafe_grupo_a, cafe_grupo_b)

#elaborar una funcion para declar o crear la funcion
#pregunta para diferencia las funciones
#=