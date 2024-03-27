# De manera similar a cómo la función de cadena le permite cambiar un número
# a una cadena
# las funciones de número entero y float permiten convertir cadenas en números
# Esto es muy útil para situaciones en las que desea obtener números de un
# usuario utilizando la función de entrada en lugar de cadenas
# Supongamos que queremos obtener un número entero de un usuario, podríamos
# hacerlo creando una variable y asignándole una llamada a la función de entrada
user_int = int(input("Dame un numero entero"))
print(user_int)
print(type(user_int))

# print(int("strings 4nd $ymbo!s"))
# print(int("5.5"))
# print(int(5.8))

# La función float() te permite convertir una cadena en un decimal
# Funciona de forma similar a la función entera
user_float = float(input("Dame un numero decimal"))
print(user_float)
print(type(user_float))

# print(float("strings 4nd $ymbo!s"))
# print(float("5.5"))
# print(float(5.8))