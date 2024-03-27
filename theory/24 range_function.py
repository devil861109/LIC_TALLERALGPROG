# Range es una función que devuelve una secuencia de números y generalmente se
# usa para iterar con un bucle for
# Puede tomar tres argumentos, inicio, parada y paso, y puede usarse con uno,
# dos o los tres al mismo tiempo

one_input = range(5)
print(one_input)

# Para este ejemplo, eso significa que la secuencia de números asignados a la
# variable una entrada comienza en cero y aumenta en uno hasta llegar a uno
# menos que cinco, que es cuatro

for num in one_input:
    print(num)

# Llamar al rango con dos argumentos crea y devuelve una secuencia de números
# que comienza en el primer argumento y aumenta en uno hasta que se detiene en
# uno menos que el segundo argumento
    
two_inputs = range(5, 10)
print(two_inputs)

for num in two_inputs:
    print(num)

# Cuando se llama al rango con tres argumentos, crea una secuencia de números
# que comienza en el primer argumento, aumenta o disminuye en el tercer
# argumento y termina en uno menos que el segundo argumento
# El tercer argumento, también conocido como tamaño de paso, se puede utilizar
# para incrementar hacia abajo, ya que puede ser negativo
    
three_inputs = range(1, 20, 3)
print(three_inputs)

# This example creates a sequence of numbers that starts at one and goes up
# by steps of three. 19 is the last number in the sequence

for num in three_inputs:
    print(num)