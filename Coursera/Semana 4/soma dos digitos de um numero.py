num = int(input("Digite um número inteiro: "))
soma = 0

while num > 0:
    ultimo = num%10
    soma = soma + ultimo
    num = num//10
    
print(soma)

