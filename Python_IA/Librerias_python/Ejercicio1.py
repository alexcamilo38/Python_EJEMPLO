import numpy as np
numeros = np.array([10,20,30,40,50])
print(numeros)
print(numeros + 2)
print(numeros * 2)
print(numeros / 10)

print('--------------------------------------------------')
#las notas son 
import numpy as np
notas = np.array([
                 [3.5,5.0,3.2,4.5,4.8],
                 [3.2,4.4,3.8,3.3,5.0],
                 [3.9,4.0,2.1,3.0,5.0]
                 ])
print('las notas son')
print(notas.mean(axis=0))

#AXIS 1 ES EN ILERA 
#AXIOS 0 ES ASIA ABAJO

print('----------------------------------------')

import numpy as np
calificacion = np.array([
    [8.5,7.0,9.0],
    [6.0,7.5,8.0]
])
print('las calificaciones')
print(calificacion.shape)
print(calificacion[0])
print(calificacion[:,0])