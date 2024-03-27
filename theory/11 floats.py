# Mas con decimales

print(1.23 + 2.80)

# ¿Por qué las expresiones que involucran flotadores producen resultados
# inexactos?
# Evitar errores de aproximación flotante
# Hay 2 formas de evaluar correctamente

# 1. Utilice números enteros en lugar de flotantes (10, 100, 1000)
ex2 = (123 + 280) / 100
print(ex2)

# Usar round()
# round() es otra FUNCION de redondeo

ex3 = 1.23 + 2.80
print(round(ex3, 2))

# Una función anidada es una función que está completamente contenida
# dentro de una función principal