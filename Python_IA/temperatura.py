temperatura=[22,18,30,25,26,20]
temperatura.append(20.5)
temperatura[4]=16
temperatura.remove(18)

promedio = sum(temperatura)/ len(temperatura)
maximo= max(temperatura)
minimo= min(temperatura)
print("Promedio",promedio)
print("Maximo",maximo)
print("minimo",minimo)