# Guardamos el valor del ángulo en grados
grados = 120

# Comprobamos si el ángulo es menor de 90 grados
if grados < 90:
    print(grados, "grados: ángulo agudo")

# Comprobamos si el ángulo es exactamente igual a 90 grados
elif grados == 90:
    print(grados, "grados: ángulo recto")

# Si no es menor ni igual a 90, entonces es mayor de 90
else:
    print(grados, "grados: ángulo obtuso")