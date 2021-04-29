num = int(input("Digite um número inteiro: "))

milhar = num//1000
mil = (num%10000)//1000
centena = ((num%10000)%1000)//100
dezena = (((num%10000)%1000)%100)//10
unidade = (((num%10000)%1000)%100)%10

print("O dígito das dezenas é",dezena)
