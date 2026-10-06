lis = ['be','ab','cc','aa','cb']
lis.sort()

print(lis)


# esta le da prioriada al las mayusculas
lis = ['aA','ab','Cc','ca']
print(sorted(lis))


#este lo organiza por minusculas es prioridad
lis = ['aA','ab','Cc','ca']
print(sorted(lis, key=str.lower))