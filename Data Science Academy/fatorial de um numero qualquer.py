# Fatorial de um numero qualquer


def fatorial(numero):

    fatorial=1
    
    while numero >= 1:
        fatorial = fatorial*numero
        numero -= 1

    return fatorial


print(fatorial(5))
 
