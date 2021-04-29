# Soma de numeros informados pelo usuario


i = 1
soma = 0

parada = int(input("Informe quantas vezes deseja executar: "))

while i <= parada:
    numero = int(input("Informe um numero: "))
    soma = soma + numero
    i += 1
    
print("Soma: ",soma)
