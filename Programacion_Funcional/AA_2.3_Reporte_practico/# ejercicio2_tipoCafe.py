# ejercicio3_tipoCafe

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    porciones = [preparar_alimento() for _ in range(cantidad)]
    precios = list(map(lambda x: precio_unitario, porciones))
    promo = calcular_promocion(cantidad)
    
    return porciones, precios, promo