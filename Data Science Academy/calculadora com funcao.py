'''
Declaração das funções de cada tipo de operaçao
'''

def soma(x,y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y


print("########## PYTHON CALCULATOR ##########")
print()
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print()

opcao = int(input("Selecione o número da operação desejada: "))

print()

x = int(input("Informe o primeiro numero: "))
y = int(input("informe o segundo numero: "))

print()

if opcao == 1:
    print("A soma é:",soma(x, y))  
elif opcao == 2:
    print("A subtração é:",subtracao(x, y))
elif opcao == 3:
    print("A multiplicação é:",multiplicacao(x, y))
elif opcao == 4:
    print("A divisão é:",divisao(x, y))
else:
    print("A opção informada não é válida")
    
