# Melhorar o programa com equação do segundo grau

import math

a = float(input("Informe o valor da variável a: "))
b = float(input("Informe o valor da variável b: "))
c = float(input("Informe o valor da variável c: "))

delta = b**2 - (4*a*c)

if delta == 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    print("a raiz desta equação é",raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        if raiz1 > raiz2:
            print("as raizes da equaçao são",raiz2,"e",raiz1)
        else:
            print("as raizes da equaçao são",raiz1,"e",raiz2)
    
