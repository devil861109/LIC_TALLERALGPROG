# Como has aprendido, cada uno de los caracteres de una cadena tiene su
# propio número de índice
# Cada elemento de una lista también tiene su propio número de índice
# Al igual que con las cadenas, los números de índice en una lista también
# comienzan en cero

indexes_example = ["java", "javascript", "python", "pascal"]
print(indexes_example)
print(indexes_example[0])

indexes_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_matrix[0][0])

# Si bien los números de índice en las listas comienzan en cero y aumentan en
# uno por cada elemento adicional, se puede usar un entero negativo al acceder
# por índice en Python
# El acceso por índice usando un número entero negativo comienza desde el
# final de una lista y va hacia atrás

print(indexes_example[-1])


mixed = [False, 365, 4.24, "string"]
print(mixed[1] + 2)
print("Accedemos > ", mixed[2])

# Si solo desea obtener una porción específica de una lista, puede hacerlo
# usando la división de listas para obtener una porción de esa lista, tal
# como obtendría porciones de una cadena
# Pero cuando divides una lista, obtienes una lista formada por un segmento
# de otra lista más grande en lugar de una cadena más pequeña formada por
# caracteres de otra cadena más grande

# Para obtener un segmento de lista, siempre comienza escribiendo el nombre de
# la lista de la que desea obtener el segmento seguido de corchetes, tal como
# lo haría al acceder a un valor de una lista por índice

# Sin embargo, la división de listas difiere del acceso por índice en que
# para obtener una división de lista siempre también se escriben dos puntos
# entre corchetes en lugar de solo un número de índice

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

example = [2, 4, 6, 8, 0]
print(example)
example[4:7] = [7, 6, 5]
print(example)