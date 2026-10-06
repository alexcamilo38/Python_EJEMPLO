def calcular_pago(horas,tarifa_hora=2000):
    if horas > 8:
        return 10000
    return horas * tarifa_hora
print(calcular_pago(4))
print(calcular_pago(10))
