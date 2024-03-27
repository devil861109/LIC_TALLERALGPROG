# Una lista es un tipo de datos que contiene múltiples valores en una secuencia
# ordenada
# Los valores dentro de una lista también se conocen como elementos
# Las listas se pueden asignar a variables como cualquier otro tipo de datos
# Para crear una lista, escriba corchetes y luego los elementos que desee que
# estén en la lista separados por comas que tengan espacios después
# Puede tener números enteros, flotantes, cadenas, valores booleanos y otras
# listas como elementos dentro de una lista

example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [2.718, 9.31]
example_list_3 = ["azul", "verde", "negro", "rojo", "amarillo"]
example_list_4 = [True, False, True, False, False]
example_list_5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(example_list_1)
print(type(example_list_1))

# La función de lista toma un tipo de datos iterable, como una cadena,
# como argumento y lo convierte en una lista que luego devuelve
# Por ejemplo, si llamamos a la función de lista con la cadena bla como
# argumento, entonces se devolverá la lista compuesta por los caracteres
# B, L, A y H

print(list("blah"))

# Los operadores in y not in se pueden utilizar para comprobar si un valor
# está o no en una lista

checked_list = [1, 2, 3, 4]
print(1 in checked_list)
print(8 in checked_list)

# Tenga en cuenta que cuando se usan en expresiones, los operadores in y not in
# se evalúan hasta valores booleanos
not_in_example = 8 not in checked_list
print(not_in_example)