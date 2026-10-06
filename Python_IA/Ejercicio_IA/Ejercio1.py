def calcular(nota):
    if nota >4.5:
        return 'Medalla de oro'
    elif nota >=4.0:
        return 'Medalla de plata'
    elif nota >=3.8:
        return 'Medalla de bronce'
    else:
        return 'sim medalla'
        
print(calcular(3.2))