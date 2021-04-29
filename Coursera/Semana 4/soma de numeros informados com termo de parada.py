# Soma de numeros informados pelo usuario

numero = int(input("Informe um numero (zero para terminar): "))
soma = 0

while (numero != 0):
    soma = soma + numero
    numero = int(input("Informe um numero: "))
    
print("Soma: ",soma)
