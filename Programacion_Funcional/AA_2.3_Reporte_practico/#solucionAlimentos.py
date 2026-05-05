#solucionAlimentos

# 1. FUNCIONES
def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"

def preparar_cafe():
    return "☕ cafe"

def preparar_hamburguesa():
    return "🍔 hamburguesa"

def preparar_taco():
    return "🌮 taco"


def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    return ""

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    porciones = [preparar_alimento() for _ in range(cantidad)]
    precios = list(map(lambda x: precio_unitario, porciones))
    promo = calcular_promocion(cantidad)
    return porciones, precios, promo


cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))
cantidad_cafes   = int(input("¿Cuántos cafés deseas ordenar? "))
cantidad_hamburguesas = int(input("¿Cuántas hamburguesas deseas ordenar? "))
cantidad_tacos    = int(input("¿Cuántos tacos deseas ordenar? "))


orden_pizza = tomar_orden(preparar_pizza, cantidad_pizzas, 25)
orden_agua  = tomar_orden(preparar_agua, cantidad_aguas, 10)
orden_tamal = tomar_orden(preparar_tamal, cantidad_tamales, 15)
orden_cafe  = tomar_orden(preparar_cafe, cantidad_cafes, 12)
orden_hamburguesa = tomar_orden(preparar_hamburguesa, cantidad_hamburguesas, 20)
orden_taco    = tomar_orden(preparar_taco, cantidad_tacos, 8)



# 4. DESEMPAQUETAR
porciones_pizza, precios_pizza, promo_pizza = orden_pizza
porciones_agua, precios_agua, promo_agua = orden_agua
porciones_tamal, precios_tamal, promo_tamal = orden_tamal
porciones_cafe, precios_cafe, promo_cafe = orden_cafe
porciones_hamburguesa, precios_hamburguesa, promo_hamburguesa = orden_hamburguesa
porciones_taco, precios_taco, promo_taco = orden_taco

# 5. PRINT
print("\n========== RESUMEN DEL PEDIDO ==========")

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print(f"\n☕ CAFES    → {porciones_cafe}")
print(f"💲 Precios  → {precios_cafe}")
print(f"🎁 Promo    → {promo_cafe if promo_cafe else 'sin promoción'}")

print(f"\n🍔 HAMBURGUESAS → {porciones_hamburguesa}")
print(f"💲 Precios  → {precios_hamburguesa}")
print(f"🎁 Promo    → {promo_hamburguesa if promo_hamburguesa else 'sin promoción'}")

print(f"\n🌮 TACOS    → {porciones_taco}")
print(f"💲 Precios  → {precios_taco}")
print(f"🎁 Promo    → {promo_taco if promo_taco else 'sin promoción'}")



print("\n========================================")