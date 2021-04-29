'''
O número de combinações possíveis de m elementos em grupos
de n elementos (n <= m) é dada pela fórmula de combinação
m!/((m-n)!n!). Escreva um programa que lê dois inteiros
m e n e calcula a combinação de m, n a n.
'''

m = int(input("Informe m: "))
n = int(input("Informe n: "))
diferenca = m-n

fat1 = 1
fat2 = 1
fat3 = 1

#Fatorial de m:
while m >= 1:
    fat1 = fat1 * m
    m -= 1
    
#Fatorial de n:
while n >= 1:
    fat2 = fat2 * n
    n -= 1
    
#Fatorial da diferença:
while diferenca >= 1:
    fat3 = fat3 * diferenca
    diferenca -= 1

combinacao = fat1/(fat3 * fat2)

print("A combinação é:",combinacao)
