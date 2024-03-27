# Cuando se usa después de declaraciones if y otras declaraciones de control
# de flujo, la declaración else permite a los programadores
# para proporcionar a sus programas el código que se ejecutará si las condiciones
# de ninguna otra declaración de control de flujo se han evaluado como verdaderas

# Hay tres partes que toda declaración else debe tener, la palabra else,
# dos puntos y el código a ejecutar

# Al igual que el código para las declaraciones if, este código también debe
# tener una sangría de cuatro espacios (space bar) o tecla TAB
# Esto es para indicarle a Python que el código está asociado con las
# declaraciones else

veg = input("Dame el nombre de un vegetal")
if (veg == "tomate"):
    print("Es un ", veg, "!!!")
else:
    print("Es otro vegetal!!", veg)
    
# NOTA: puede existir el IF sin el ELSE, pero no puede existir el ELSE sin el IF
# hay jerarquía