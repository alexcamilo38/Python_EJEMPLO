import numpy as np
estudiante = np.array([
    [8.5,7.0,9.0],
    [6.0,7.5,8.0],
    [3.5,5.0,3.2],
    [3.9,4.0,5.0]
])
pMateria = estudiante.mean(axis=0)
pEstudiante = estudiante.mean(axis=1)
print(pMateria)
print(pEstudiante)
