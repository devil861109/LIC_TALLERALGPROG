# En programación, habrá ocasiones en las que poder reutilizar código en
# diferentes variables y valores sin tener que reescribirlo le ahorrará una
# cantidad significativa de tiempo y le permitirá usar mucho menos código
# Las funciones permiten a los programadores hacer esto
# Supongamos que tiene algún código, como estas cuatro declaraciones impresas,
# que desea ejecutar varias veces

print("Esto")
print("Es ")
print("Un")
print("Ejemplo")

# Podrías hacerlo copiando y pegando el código tantas veces como necesites
# para ejecutarlo, pero eso requeriría muchas líneas de código
# El punto principal de las funciones es brindar a los programadores la
# capacidad de evitar tener que duplicar código como este

def prints_four():
    print("Esto")
    print("Es ")
    print("Un")
    print("Ejemplo")

def function_name():
    print(2 + 2)


# Las funciones no ejecutan automáticamente su código después de su creación
# Para usar una función, debes llamarla. Para llamar a una función, escriba
# su nombre seguido de paréntesis
    
prints_four()

function_name()

# Un parámetro es un nombre de marcador de posición para la variable o los
# datos en los que desea que su función ejecute su código
# Cuando crea un parámetro, va entre paréntesis de una función y recibe un
# nombre que sigue las mismas reglas y convenciones de nomenclatura que
# los nombres de variables y funciones

def imprime_mensaje(mensaje):
    print(mensaje)

imprime_mensaje("Esto es un mensaje")

# Una función puede tener tantos parámetros entre paréntesis como desee,
# siempre y cuando cada uno de ellos esté separado por una coma seguida
# de un espacio

def suma_tres_numeros(a, b, c):
    print(a + b + c)

suma_tres_numeros(1, 2, 3)

# Para dar parámetros predeterminados a una función, simplemente establezca
# los parámetros iguales a los que desee que sean los valores predeterminados

def suma_tres_numeros_otro(a=1, b=2, c=3):
    print(a + b + c)

suma_tres_numeros_otro()

# Si desea usar el resultado de la llamada a la función en lugar de simplemente
# mostrar algo en la salida, necesitará usar la palabra clave return y asignar
# una llamada a una variable como esta o usar una llamada en una expresión

def suma_tres_numeros_regreso(a=1, b=2, c=3):
    return a + b + c

suma = suma_tres_numeros_regreso()
print(suma)