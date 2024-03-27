# La declaración elif, también conocida como declaración else/if, es una
# declaración que le permite proporcionar tantas condiciones adicionales
# para verificar como necesites sin el desorden que conlleva tener que usar
# múltiples declaraciones if anidadas y bloques de declaración if/else
    
edad = int(input("Dame tu edad"))
if (edad >= 18):
    print("Eres mayor de edad")
    if edad < 25:
        print("Eres adulto joven")
    elif edad >= 25 and edad < 40:
        print("Eres adulto responsable")
    elif edad >= 40 and edad < 60:
        print("Eres adulto maduro")
    else:
        print("Eres adulto senior!")
else:
    print("Eres menor de edad")
    if edad < 13:
        print("Eres un infante")
    else:
        print("Eres un adolescente")