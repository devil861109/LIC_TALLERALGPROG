# La función de entrada, que le permitirá hacer que sus programas obtengan
# y utilicen la entrada de un usuario
# No importa cuál sea la función de entrada que se proporcione como entrada,
# siempre devuelve una cadena
name = input("Dame tu nombre\n")
print(name)
print(type(name))

# Si el usuario ingresa un número entero como su número favorito, podrá ver que
# el tipo de datos asignados a fav_num es una cadena en lugar de un número entero
# Si ejecuto el programa nuevamente e ingreso un valor flotante, a fav_num
# todavía se le asigna una cadena
fav_num = input("Dame tu numero favorito")
print(fav_num)
print(type(fav_num))