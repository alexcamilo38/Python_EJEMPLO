Estudiante = [
    {
        "nombre": "camila",
        "curso": "Python Basico",
        "nota": 4.5,
        "aprovado": True
    },
    {
        "nombre": "David",
        "curso": "Python Basico",
        "nota": 4,
        "aprovado": True
    },
    {
        "nombre": "Samuel",
        "curso": "Python Basico",
        "nota": 4.2,
        "aprovado": True
    }
]


Estudiante[1]["nota"] = 5


for estudiante in Estudiante:
    for clave, valor in estudiante.items():print(clave, valor)