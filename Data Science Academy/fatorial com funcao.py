#Resolver o programa 'varios fatoriais que poderiam ser resolvidos com funcao' com função:


def fatorial(numero):

    fatorial=1
    
    while numero >= 1:
        fatorial = fatorial*numero
        numero -= 1

    return fatorial



def combinacao(m, n):

    return fatorial(m)/(fatorial(n)*fatorial(m-n))
    
    
print("Combinaçao (4,2) = ", int(combinacao(4,2)))
print("Combinaçao (5,2) = ", int(combinacao(5,2)))
print("Combinaçao (10,4) = ", int(combinacao(10,4)))
