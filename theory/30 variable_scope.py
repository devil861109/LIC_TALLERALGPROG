# En Python, puedes tener una variable dentro de una función que tenga el
# mismo nombre que una variable fuera de esa función
# Sin embargo, a pesar de tener el mismo nombre, esas variables no son la
# misma variable
# Para comprender cómo funciona esto, es necesario conocer el alcance global
# y local

example = "Hello World"

def local_function():
    example = "Good Bye World!"
    return example

print(example)
print(local_function())