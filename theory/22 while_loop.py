# Los bucles son una herramienta útil cuando desea ejecutar código en cada
# elemento de un dato que tiene índices como una cadena; en esta lección,
# aprenderá sobre un tipo de bucle conocido como bucle while
# Igual nos sirven para saber cuantas veces se ejecuta cierto código repetitivo
# Repasaremos la sintaxis de un bucle while y luego explicaremos qué hace
# Un bucle while tiene cuatro partes, la palabra while, una condición
# que se evalúa como un valor booleano, y dos puntos
# Dentro del bucle while, debe haber identación
# En el momento que termina la identación, en ese momento se especifica que 
# lo que ya no está identado no pertenece a la evaluación del bucle

counter = 0

while counter < 3:
    print(counter)
    counter += 1

# Hablemos de bucles infinitos, los bucles infinitos son solo bucles que
# ejecutan su código, una cantidad infinita de veces y, por lo tanto, nunca
# terminan debido a esto
# Debes asegurarte de que cada bucle while que crees tenga una condición que
# le impida ejecutar su código una cantidad infinita de veces, un bucle while
# que tenga un final causado por su condición