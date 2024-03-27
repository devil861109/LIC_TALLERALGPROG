# Cuando utilices bucles while, no siempre sabrás cuántas veces el bucle
# ejecutará su código antes de finalizar
# Para realizar un número fijo de iteraciones, el bucle for es particularmente
# útil porque es un tipo de bucle que está controlado por la longitud del dato
# iterable en el que se utiliza en lugar de una condición

# Para crear un bucle for, necesita seis cosas, la palabra for, un nombre de
# variable para contener un elemento del elemento que se está iterando,
# la palabra in, el elemento que se está iterando, dos puntos y luego el
# código que ejecutará el bucle for. en cada elemento de aquello por lo que
# se está iterando

word = "house"
for letter in word:
    print(letter)

# iterar desde i = 0 a i = 3
for i in range(4):
    print(i)

for x in range(2, 6):
    print(x)