#Função para calculo de Fatorial

def fatorial(numero):

    fatorial = 1
    
    for i in range(1, numero+1):
        if i <= numero:
            fatorial *= i

    return fatorial

print(fatorial(5))
