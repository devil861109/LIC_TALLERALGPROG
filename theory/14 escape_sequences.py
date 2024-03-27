# Las secuencias de escape son caracteres especiales que puedes usar en cadenas
# que te permiten hacer cosas como insertar comillas dentro de ellas y hacer
# que aparezcan diferentes partes de las cadenas en diferentes líneas de salida

# El carácter de tabulación está representado por una barra invertida seguida
# de una t minúscula
# Se utiliza para hacer un espacio horizontal o sangría cuando se trabaja
# con cadenas
print("This\tis\ta\tlot\tof\tspace")

# El carácter de nueva línea está representado por una barra invertida
# seguida de una n minúscula
# Se utiliza para colocar lo que se escribe después en una nueva línea
# justo debajo de la actual
print("Line one\nLine two")

# Para poner comillas en sus cadenas, usaría secuencias de escape de comillas
# simples o dobles dependiendo de si incluye sus cadenas entre comillas
# simples o dobles

print("This is a simple \'Example\' of quotes")
print("This is another simple \"Example\" of quotes")

# La secuencia de escape de barra invertida se usa siempre que desee colocar
# una barra invertida en una cadena
print("Using a backslash \\ in our string")