totalseg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = int(totalseg/86400)
horas = int((totalseg%86400)/3600)
minutos = int(((totalseg%86400)%3600)/60)
segundos = int(((totalseg%86400)%3600)%60)

print(dias,"dias,", horas,"horas,",minutos,"minutos e",segundos,"segundos.")
