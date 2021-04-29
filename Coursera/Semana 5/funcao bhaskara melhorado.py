# Melhorar o programa com equação do segundo grau

import math

def recebeValor():
    '''
    Função para exibir uma mensagem na tela e
    receber um valor 
    '''
    return int(input("Informe um valor: "))


def raizReal(b, delta, a):
    '''
    Função para calcular as raizes reais
    '''
    return (-b + math.sqrt(delta))/(2*a)



# Recebendo valores através da função recebeValor()
a = recebeValor()
b = recebeValor()
c = recebeValor()

# Calculo de Delta:
delta = b**2 - (4*a*c)

if delta == 0:
    raiz = raizReal(b, delta, a)
    print("a raiz desta equação é",raiz)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = raizReal(b, delta, a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        if raiz1 > raiz2:
            print("as raizes da equaçao são",raiz2,"e",raiz1)
        else:
            print("as raizes da equaçao são",raiz1,"e",raiz2)
