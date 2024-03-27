# Una cadena es solo una secuencia de caracteres
# Esos caracteres pueden ser cualquier combinación de números, espacios,
# letras mayúsculas, minúsculas, guiones bajos o símbolos, como un punto o un
# signo de exclamación
# Para crear una cadena, simplemente escriba lo que quiera que sea la cadena
# entre comillas simples o dobles
# No existe una diferencia significativa entre cadenas entre comillas simples
# y cadenas entre comillas dobles
# Sin embargo, prefiero encerrar mis cadenas entre comillas dobles ya que si
# usas comillas dobles, puedes usar comillas simples dentro de las cadenas sin
# tener que usar secuencias de escape

ex_1 = 'This is a string'
ex_2 = "This is another string"

ex_3 = '1984!'
ex_4 = "LiVe LONG and PRosPEr."
ex_5 = "!@#$%^&*()_-=+=/.,?><:;{}[]`|"
ex_6 = ""
ex_7 = " "

ex_8 = "001234"

# Accediendo a caracteres por índice

ex_9 = "orange"
print(ex_9)
print(ex_9[1])

print("apple"[4])

# En ARRAYS empezamos a contar en CERO 0

# Cortar cadenas (String slicing)

# El slice de cadenas le permite obtener partes de una cadena y asignarlas
# a variables o imprimirlas
# donde un segmento de una cadena es solo una cadena que originalmente
# era parte de otra cadena
# "tomate"
# "toma"
# Por ejemplo, "toma" es un slice de la cadena "tomate"

# Hay tres formas de cortar una cadena
ex_10 = "apricots"
# Desde su inicio hasta cierto punto, como en el primer ejemplo
print(ex_10[:3])
# Desde un punto inicial hasta un punto final, como en el segundo ejemplo,
print(ex_10[2:5])
# Y desde un punto inicial hasta el final de la cadena, como en el tercer
# ejemplo
print(ex_10[4:])

# Para cortar una cadena desde su inicio hasta un punto determinado, escriba
# el nombre de la variable que contiene la cadena que desea cortar o la cadena
# que desea cortar, luego corchetes, dos puntos, y después de los dos puntos,
# uno más que el índice del último carácter de la cadena que quieres que este
# en el slice

# Concatenación

# Las cadenas también se pueden sumar usando el operador de suma en un proceso
# conocido como concatenación
print("pecan" + " " + "pie")

concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)