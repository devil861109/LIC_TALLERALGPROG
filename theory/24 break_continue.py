# En programación, las declaraciones break y continue se utilizan para
# alterar el flujo de bucles:
# break sale del bucle por completo
# continue omite la iteración actual y pasa a la siguiente

# La declaración break finaliza el ciclo inmediatamente cuando se encuentra
# Sintaxis: break

# Podemos usar la declaración break con el bucle for para finalizar el
# bucle cuando se cumple una determinada condición. Por ejemplo

for i in range(5):
    if i == 3:
        break
    print(i)

# La instrucción continuar omite la iteración actual del bucle y el flujo
# de control del programa pasa a la siguiente iteración
# Sintaxis: continue

# Podemos usar la instrucción continue con el bucle for para omitir la
# iteración actual del bucle y saltar a la siguiente iteración. Por ejemplo

for i in range(5):
    if i == 3:
        continue
    print(i)