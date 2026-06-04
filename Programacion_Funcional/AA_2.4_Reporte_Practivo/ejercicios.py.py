
# Ejercicio 3: Inflar globos


# 1. Función normal
def inflar_globo():
    return "🎈"

# 2. Función lambda
inflar_globo_lambda = lambda: "🎈"

# 3. Lista de globos con lambda y comprensión de listas
numero_invitados = int(input("¿Cuántos invitados van a la fiesta? "))
globos_lambda = [inflar_globo_lambda() for _ in range(numero_invitados)]

# 4. Función preparar_globos
def preparar_globos(numero_invitados):
    return [inflar_globo() for _ in range(numero_invitados)]

# 5. Llamada y resultado
globos_fiesta = preparar_globos(numero_invitados)
print(globos_fiesta)



# Ejercicio 4: Mostrar el menú de la cafetería

menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50,
}

def ver_menu(menu):
    return [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]

menu_formateado = ver_menu(menu)

for item in menu_formateado:
    print(item)



# Ejercicio 4b: La cuenta de la cafetería

from functools import reduce

orden = [25.50, 22.00, 35.75, 40.00, 18.50]

# map(): aplicar 10% de descuento
precios_con_descuento = list(map(lambda precio: precio * 0.90, orden))
print(precios_con_descuento)

# filter(): solo bebidas con precio > $25 (después del descuento)
bebidas_caras = list(filter(lambda precio: precio > 25, precios_con_descuento))
print(bebidas_caras)

# reduce(): total a pagar
total = reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
print(f"Total a pagar: ${total:.2f}")
