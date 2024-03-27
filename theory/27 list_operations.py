# Las declaraciones Del le permiten eliminar valores de una lista.

planets = ["pluton", "tierra", "venus", "jupiter"]
print(planets)
del planets[0]
print(planets)

# El método remove permite eliminar lo que le pasas como argumento de una lista

planets = ["pluton", "tierra", "venus", "jupiter"]
print(planets)
planets.remove("pluton")
print(planets)

# La diferencia entre del y remove es que del elimina un elemento según el
# número de índice del elemento que se elimina
# Mientras que el método remove busca en una lista cualquier elemento que le
# hayas pasado como argumento y lo elimina de la lista cuando encuentra ese
# elemento

# Así que remove se deshace de un elemento específico si lo encuentra,
# independientemente de dónde se encuentre dentro de una lista, mientras que
# del simplemente elimina un elemento de un índice

# El método append toma un argumento y agrega dicho valor al final de la lista
# Si quisiéramos agregar algo al final de esta lista, podríamos escribir su
# nombre, .append, paréntesis y luego el elemento que queremos que se agregue
# al final de la lista

pets = ["perro", "gato", "tortuga"]
print(pets)
pets.append("serpiente")
print(pets)

# Insertar es similar a agregar en que se usa para agregar un elemento
# a una lista
# Sin embargo, a diferencia de agregar, insertar le permite agregar un
# elemento en cualquier lugar de la lista en lugar de solo al final
# Para hacer esta inserción se necesitan dos argumentos donde el primer
# argumento es el índice en el que se agregará un nuevo elemento a una lista,
# y el segundo argumento es el elemento que se agregará a la lista en ese índice

pets = ["perro", "gato", "tortuga"]
print(pets)
pets.insert(0, "serpiente")
print(pets)

# El método de clasificación se puede utilizar para ordenar listas formadas
# por elementos que son todos números o elementos que son solo cadenas

num_list = [2.718, 4, -19, 1000, 0]
print(num_list)
num_list.sort()
print(num_list)

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()
print(str_list)

# También puedes escribir reverse=True entre paréntesis del método de
# clasificación cuando lo llamas para ordenar elementos de una lista en orden
# inverso

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort(reverse=True)
print(str_list)

# El método de clasificación no se puede utilizar en listas mixtas formadas
# por diferentes tipos de datos ya que no sabe cómo comparar cadenas y números
# entre sí

# El método de lista de índice le permite averiguar el número de índice del
# elemento que le pasa

metals = ["oro", "plata", "bronce"]
print(metals.index("bronce"))

# Podemos saber la longitud de una lista con la función len()
print(len(metals))