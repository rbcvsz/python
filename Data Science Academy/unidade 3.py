# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
var1 = 4

while var1 <=20:
    if var1%2 == 0:
        lista.append(var1)
    var1 += 1

print(lista)
