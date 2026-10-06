class Parqueadero:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []
        self.historial = []
        self.tarifas = {"carro": 3000, "moto": 1500, "bicicleta": 1000}

    def validar_placa(self, placa):
        return len(placa) == 6

    # Ingresar vehículo
    def ingresar_vehiculo(self, tipo, placa):
        tipo = tipo.lower()
        placa = placa.upper()

        if tipo not in self.tarifas:
            print("Tipo de vehículo no válido.")
            return
        if not self.validar_placa(placa):
            print("La placa debe tener 6 caracteres.")
            return
        if len(self.vehiculos) >= self.capacidad:
            print("El parqueadero está lleno.")
            return

        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                print("El vehículo ya está ingresado.")
                return

        vehiculo = {"tipo": tipo, "placa": placa}

        self.vehiculos.append(vehiculo)
        print("Vehículo ingresado correctamente.")

    # Retirar vehículo y cobrar
    def retirar_vehiculo(self, placa):
        placa = placa.upper()

        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                cobro = self.tarifas[vehiculo["tipo"]]

                registro = {
                    "tipo": vehiculo["tipo"],
                    "placa": vehiculo["placa"],
                    "cobro": cobro,
                }

                self.historial.append(registro)
                self.vehiculos.remove(vehiculo)

                print("Vehículo retirado correctamente.")
                print("Total a pagar: $", cobro)
                return

        print("El vehiculo no se encuentra en el parqueadero.")

    # Mostrar vehículos actuales
    def mostrar_vehiculos(self):
        if len(self.vehiculos) == 0:
            print("No hay vehiculos en el parqueadero.")
            return

        print(" Vehiculos en el parqueadero")

        for vehiculo in self.vehiculos:
            print("Tipo:", vehiculo["tipo"], " Placa:", vehiculo["placa"])

    # Mostrar historial
    def mostrar_historial(self):
        if len(self.historial) == 0:
            print("No hay registros en el historial.")
            return

        print("Historial de vehiculo")

        for registro in self.historial:
            print(
                "Tipo:",
                registro["tipo"],
                "Placa:",
                registro["placa"],
                "Cobro: $",
                registro["cobro"],
            )

    # Total recaudado
    def total_recaudado(self):
        total = 0

        for registro in self.historial:
            total += registro["cobro"]

        print("Total recaudado: $", total)

    # Recaudado por tipo
    def recaudado_por_tipo(self):
        totales = {"carro": 0, "moto": 0, "bicicleta": 0}

        for registro in self.historial:
            tipo = registro["tipo"]
            totales[tipo] += registro["cobro"]

        print(" RECAUDADO POR TIPO ")
        for tipo, total in totales.items():
            print(tipo.capitalize(), ": $", total)


# Programa principal
parqueadero = Parqueadero(10)

while True:
    print(" SISTEMA DE PARQUEADERO")
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Ver vehículos")
    print("4. Ver historial")
    print("5. Total recaudado")
    print("6. Recaudado por tipo")
    print("7. Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tipo = input("Tipo (carro, moto, bicicleta): ")
        placa = input("Ingrese la placa: ")
        parqueadero.ingresar_vehiculo(tipo, placa)

    elif opcion == "2":
        placa = input("Ingrese la placa del vehículo: ")
        parqueadero.retirar_vehiculo(placa)

    elif opcion == "3":
        parqueadero.mostrar_vehiculos()

    elif opcion == "4":
        parqueadero.mostrar_historial()

    elif opcion == "5":
        parqueadero.total_recaudado()

    elif opcion == "6":
        parqueadero.recaudado_por_tipo()

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
