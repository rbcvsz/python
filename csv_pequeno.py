import csv

#Abrir o arquivo
referencia = open(r"C:\python\pequeno3.csv","r")

#Ler a tabela
arquivo = referencia.read()

#Separar o arquivo em linhas:
linhas = arquivo.split('\n')

todasLinhas = []

#Separar cada linha em coluna:
for i in linhas:
    colunas = i.split(',')
    print()
    todasLinhas.append(colunas)

print(todasLinhas)
