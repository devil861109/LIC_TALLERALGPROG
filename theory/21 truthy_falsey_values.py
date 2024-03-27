# A veces te encontrarás con un código parecido a este. Parece extraño ya que
# en lugar de tener una condición usando operadores de comparación que evalúan
# algo, aquí la declaración if solo tiene una cadena delante
# Sin embargo, este código funcionará debido a los valores de verdad y falsedad
# Para cadenas, cualquier cosa que no sea una cadena vacía es veraz

string_example = input("Dame valor")

if string_example:
    print("Hay valor")
else:
    print("No hay valor")

# Para números enteros, cero es el valor falso
# Cualquier número entero distinto de cero se valida como verdadero
# Para floats 0.0 es el valor falso
# Hay una función llamada función bool que puede indicarle el valor booleano
# equivalente de cualquier cosa que ingrese entre paréntesis

print(bool(0))
print(bool(0.0))