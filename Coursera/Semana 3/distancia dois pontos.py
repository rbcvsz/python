import math

x1 = int(input("Informe um numero: "))
y1 = int(input("Informe um numero: "))
x2 = int(input("Informe um numero: "))
y2 = int(input("Informe um numero: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
