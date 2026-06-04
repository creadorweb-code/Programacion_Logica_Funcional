#1.CREA UNA FUNCION QUE NO TOME NINGUN ARGUMENTO Y DEVUELVA LA CADENA DE TEXTO "CAFE" 
# #PARA simular LaS PREPARACION DE UNA TAZA DE CAFE

def preparar_cafe();
    return "cafe"

#2.crear funcion para tomar orden de cafe que tome un argumento numero_tazas, que indica cuantas tazas de cafe se desean
#dentro de la funcion:
--almacena los resultados en una lista llamada

def ordenar_cafe(numero_tazas):
    tazas_cafe =[preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = ordenar_cafe(10)

print(cafe_para_grupo)





