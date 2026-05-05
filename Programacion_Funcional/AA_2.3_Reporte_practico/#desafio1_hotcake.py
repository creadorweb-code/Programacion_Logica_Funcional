# desafio1_hotcake

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))
cantidad_cafes   = int(input("¿Cuántos cafés deseas ordenar? "))
cantidad_hamburguesas = int(input("¿Cuántas hamburguesas deseas ordenar? "))
cantidad_tacos    = int(input("¿Cuántos tacos deseas ordenar? "))

orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)
orden_cafe   = tomar_orden(preparar_cafe,   cantidad_cafes,   12)
orden_hamburguesa = tomar_orden(preparar_hamburguesa, cantidad_hamburguesas, 20)
orden_taco    = tomar_orden(preparar_taco,    cantidad_tacos,    8)

