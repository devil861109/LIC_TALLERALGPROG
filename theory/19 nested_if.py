# Habrá ocasiones en las que necesitarás colocar declaraciones if y else
# dentro de otras declaraciones if y else
# Usar declaraciones if y else de esta manera se llama anidamiento
    
edad = int(input("Dame tu edad"))
if (edad >= 18):
    print("Eres mayor de edad")
    if edad < 35:
        print("Eres adulto joven")
    else:
        print("Eres adulto senior!")
else:
    print("Eres menor de edad")
    if edad < 13:
        print("Eres un infante")
    else:
        print("Eres un adolescente")