x = 10  # valor de x
y = 20  # valor de y
z = 25  # valor de z

# comprobamos si x es el mayor
if x >= y and x >= z:
    print("El numero mayor es", x)

# comprobamos si y es el mayor
elif y >= x and y >= z:
    print("El numero mayor es", y)

# si no es x ni y, el mayor es z
else:
    print("El numero mayor es", z)