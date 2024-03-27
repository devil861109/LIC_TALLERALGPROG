# Los módulos contienen conjuntos de funciones que pueden resultar útiles
# para muchas cosas diferentes
# Para utilizar las funciones dentro de ellos, debes importarlas
# Hay tres formas diferentes de hacer esto: importaciones genéricas, funciones,
# importaciones e importaciones universales
# No importa el tipo de importación, debes comenzar escribiendo import seguido
# del nombre del módulo
# La importación de un módulo usando solo la palabra clave import y luego el
# nombre del módulo que desea importar

# Importación genérica

import random

# Random es un módulo que contiene funciones para crear elementos aleatorios,
# como flotadores aleatorios o valores enteros

print(random.randint(1,10))

# Esto significa que el número entero devuelto será mayor o igual que el
# primer argumento y menor o igual que el segundo argumento

# Importación de función

# Una importación de función es cuando se importa una función específica
# desde un módulo
# Para importar una función desde un módulo, debe escribir desde, el nombre
# del módulo desde el que se importa la función, importar y luego el nombre
# de la función que se importa

from random import randint

print(random.randint(1,10))

# Importación universal

# Una importación universal es cuando importas cada función de un módulo de modo
# que cada vez que llamas a cualquier función de ese módulo, no necesitas
# escribir el nombre del módulo y un punto
# Para realizar una importación universal, simplemente escriba desde, el
# nombre del módulo cuyo contenido desea importar, importe y, finalmente,
# un asterisco

from random import *

print (randint(1,10))