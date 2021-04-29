#Função para calculo Coeficiente Binomial

def fatorial(numero):

    '''
    Funçao para calculo do fatorial
    '''
    
    fatorial = 1
    
    for i in range(1, numero+1):
        if i <= numero:
            fatorial *= i

    return fatorial

#Entrada dos coeficientes
n = int(input("Informe o coeficiente n: "))
k = int(input("Informe o coeficiente k: "))

#Calculo do Coeficiente Binomial (mostrar somente a divisao inteira
# basta utilizar //
binomial = fatorial(n) // (fatorial(k)*fatorial(n-k))

print("Coeficiente binomial: ", binomial)
