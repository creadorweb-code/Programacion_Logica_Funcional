# =============================================================================
#  ACTIVIDAD PRÁCTICA INTEGRADORA
#  Sistema de pedidos: Comedor Escolar
# =============================================================================
#  Programación Funcional en Python — Nivel Básico
#  Temas integrados:
#    ✅ Funciones simples y de primera clase  
#    ✅ Comprensión de listas                 
#    ✅ Funciones de orden superior           
#    ✅ Callbacks                             
#    ✅ Funciones lambda + map()              
#    ✅ Lógica condicional dentro de funcs.   
#    ✅ Entrada del usuario                   
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────
# Antes de comenzar a codificar, investiga y responde en comentarios:
#
# 1. ¿Qué es una función de primera clase en Python?
#    R: Es una funcion que puede ser asignada a una variable, pasada como argumento o devuelta como valor de otra función.
#       en otras palabras, las funciones de primera clase son objetos de primera clase, lo que significa que pueden ser tratada como cualquier otro objeto de python.
#
# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
#    R: una función de orden superior es una función que puede tomar otra funcióm como argumento o devolverla como resultado, mientra que una callback es una función que
#       se pasa como argumento a otra función y se ejecuta dentro de esa función, en otras palabras, una función de orden superior es una función que puede manipular otras
#       funciones, mientras que un callback es una función que se utiliza como argumento para ser ejecutada dentro de otra función.
#
# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
#    R: cuando se desea crear una nueva lista a partir de una secuencia existente, aplicando una transformación o filtrado a cada elemento. la compresión de listas es mas
#       concisa y legible que un ciclo for tradicional, lo que facilita la escritura y comprensión del código. además, la compresión de listas suele ser más eficiente en 
#       términos de rendimiento, ya que está optimizada para crear listas de manera rápida y eficiente. en resumen, conviene usar comprensión de listas cuando de desea
#       crear una nueva lista a partir de una secuencia existente, aplicando una tranformación o filtrado de manera concisa y eficiente.
#
# 4. ¿Qué hace map() y cómo se relaciona con lambda?
#    R: map() es una función incorporada en python que se utiliza para aplicar una función a cada elemento de un iterable (como una lista) y devolver un nuevo iterable
#       con los resultados. lambda es una función anónima que se puede definir en una sola línea del código, y se utiliza comúnmente como argumento para funciones como
#      map(). la relación entre map() y lambda es que lambda se puede usar para crear funciones simples y concisas que se puede pasar como argumento a map(), lo que permite
#        aplicar una transformación o operación a cada elemento de un iterable de manera rapida y eficiente.
#
# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
#    R: pasar una función como argumento a otra función ofrece varias ventajas, entre ellas:
#       - flexibilidad: permite que una función pueda ser personalizada o adaptada a diferentes situaciones sin necesidad de modificar su código interno.
#       - reutilización: permite que una función pueda ser reutilizada en diferentes contextos, ya que se puede pasar a diferentes funciones como argumentos.4
#       - abstracción: permite que una función pueda operar a un nivel más alto de abstracción, ya que puede recibir funciones coomo argumentos y operar sobre ellas
#       - modularidad: permite que una función puede ser dividida en parte más pequeñas y manajebles, ya que se puede pasar funciones como argumentos para realizar tareas.
#         en resumen, pasar una función como argumento a otra función ofrece flexibilidad, reutilización, abstraccion y modularidad, lo que facilita la escritura del código
# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────
# Lee el siguiente escenario y diseña tu solución ANTES de codificar.
#
# ESCENARIO
# La cooperativa escolar ofrece tres productos en su menú:
#   🍕 Pizza  |  🥤 Agua fresca  |  🫔 Tamal
#
# El sistema debe:
#   A) Preparar cualquier producto usando una función dedicada por producto.
#   B) Tomar la orden de un grupo: recibir la FUNCIÓN del producto y la
#      CANTIDAD solicitada, y devolver una lista con todas las porciones.
#   C) Calcular el precio total aplicando el precio unitario a cada porción  
#      usando map() y una función lambda.
#   D) Aplicar una PROMOCIÓN: si el pedido es de 3 o más porciones,
#      agregar "🎁 postre gratis" a la orden.
#   E) Solicitar al usuario cuántas porciones desea de cada producto y
#      mostrar el resumen completo del pedido.
#
# Antes de codificar respone o describe:
#      - ¿Qué funciones necesitas definir?
#       1. preparar_pizza()
#       2. preparar_agua()
#       3. preparar_tamal()
#       4. calcular_promoción(cantidad)
#       5. tomar_orden(preparar_alimento, cantidad, precio_unitario)
#       6. calcular_precio_total(precios)
#       6. aplicar_promo(precio_total, promoción)
#       7. solicitar_cantidad(producto)
#
#      - ¿Cuál de ellas es de orden superior? ¿Por qué?
#         1. tomar_orden()
#         
#      - ¿Dónde usarás comprensión de listas?
#         1. tomar_orde() para generar la lista de porciones
#
#      - ¿Dónde usarás lambda + map()?
#         1. calcular_precio_total()
# 
# 
#
#
# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────
# Completa cada paso en el orden indicado.
# Puedes apoyarte en los archivos del carpeta para recordar la sintaxis.


# ── PASO 1 ──────────────────────────────────────────────────────────────────
# Define tres funciones simples, sin parámetros, que devuelvan el nombre
# (y emoji) del producto correspondiente. Son funciones de primera clase.
#
# Referencia: ejercicio1_cafe.py → preparar_cafe()
#             desafio2_alimentos.py → preparar_pizza(), preparar_hamburguesa()

def preparar_pizza():
    pass  # ← reemplaza pass con: return "🍕 pizza"

def preparar_agua():
    pass  # ← reemplaza pass con: return "🥤 agua fresca"

def preparar_tamal():
    pass  # ← reemplaza pass con: return "🫔 tamal"


# ── PASO 2 ──────────────────────────────────────────────────────────────────
# Define la función calcular_promocion(cantidad).
# Si cantidad >= 3, devuelve el string "🎁 postre gratis".
# En caso contrario, devuelve un string vacío "".
#
# Referencia: desafio2_alimentos.py → calcular_bonus()

def calcular_promocion(cantidad):
    pass  # ← escribe la lógica condicional aquí


# ── PASO 3 ──────────────────────────────────────────────────────────────────
# Define la función tomar_orden(preparar_alimento, cantidad, precio_unitario).
#
# Esta función es de ORDEN SUPERIOR porque recibe otra función como argumento.
# preparar_alimento → función que se usará como callback (pizza, agua o tamal)
# cantidad          → número de porciones
# precio_unitario   → costo por porción (número)
#
# Dentro de la función debes:
#   a) Usar COMPRENSIÓN DE LISTAS para generar la lista de porciones,
#      llamando a preparar_alimento() en cada iteración.
#   b) Usar map() con una función LAMBDA para calcular el precio de cada
#      porción: cada elemento de la lista recibe el precio_unitario.
#      Convierte el resultado en lista con list().
#   c) Llamar a calcular_promocion(cantidad) y guardar el resultado.
#   d) Devolver una tupla: (porciones, precios, promocion)
#
# Referencia: ejercicio2_tipoCafe.py → ordenar_cafe()
#             desafio2_alimentos.py  → ordenar_alimento()
#             compresionListas.py    → map + lambda
#             funciones.py           → callbacks y orden superior

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas
    porciones = []          # ← reemplaza con list comprehension

    # b) map() + lambda para precios
    precios = []            # ← reemplaza con list(map(lambda ..., porciones))

    # c) Promoción
    promocion = ""          # ← llama a calcular_promocion(cantidad)

    # d) Devuelve los tres valores
    return porciones, precios, promocion


# ── PASO 4 ──────────────────────────────────────────────────────────────────
# Solicita al usuario la cantidad de cada producto y toma las órdenes.
# Almacena cada resultado en una variable distinta.
#
# Referencia: desafio1_hotcake.py → input() + int()

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))
cantidad_cafes   = int(input("¿Cuántos cafés deseas ordenar? "))
cantidad_hamburguesas = int(input("¿Cuántas hamburguesas deseas ordenar? "))
cantidad_tacos    = int(input("¿Cuántos tacos deseas ordenar? "))

# Llama a tomar_orden para cada producto.
# Precios sugeridos: pizza=25, agua=10, tamal=15
orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)
orden_cafe   = tomar_orden(preparar_cafe,   cantidad_cafes,   12)
orden_hamburguesa = tomar_orden(preparar_hamburguesa, cantidad_hamburguesas, 20)
orden_taco    = tomar_orden(preparar_taco,    cantidad_tacos,    8)



# ── PASO 5 ──────────────────────────────────────────────────────────────────
# Muestra el resumen del pedido.
# Para cada orden imprime: porciones, precios y promoción (si aplica).
#
# Ejemplo de salida esperada:
#   🍕 PIZZAS   → ['🍕 pizza', '🍕 pizza', '🍕 pizza']
#   💲 Precios  → [25, 25, 25]
#   🎁 Promo    → 🎁 postre gratis
#
# Referencia: solucionAlimentos.py → print de tupla

print("\n========== RESUMEN DEL PEDIDO ==========")
# Desempaqueta cada tupla en sus tres partes y muéstralas
porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")


# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────
# Ejecuta el programa con los siguientes casos y verifica los resultados.
#
# CASO 1 — Sin promoción (cantidades menores a 3):
#   Pizzas: 2  | Aguas: 1  | Tamales: 2
#   Esperado: ninguna orden muestra "🎁 postre gratis"
#
# CASO 2 — Con promoción en todas las órdenes:
#   Pizzas: 3  | Aguas: 5  | Tamales: 4
#   Esperado: las tres órdenes muestran "🎁 postre gratis"
#
# CASO 3 — Promoción mixta:
#   Pizzas: 1  | Aguas: 3  | Tamales: 2
#   Esperado: solo la orden de aguas muestra "🎁 postre gratis"
#
# CASO 4 — Verificación de precios con map() + lambda:
#   Pide 3 pizzas a $25 c/u → la lista de precios debe ser [25, 25, 25]
#   Pide 4 tamales a $15 c/u → la lista de precios debe ser [15, 15, 15, 15]
#
# Registra:
#   - ¿El resultado coincide con lo esperado? ✅ 
#   - Si no coincide, ¿en qué función está el error? ninguna
#   - ¿Qué cambiarías para corregirlo? nada
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.
# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().
# ─────────────────────────────────────────────────────────────────────────────
