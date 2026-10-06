class carrito_compra:
    def __init__(self):
        self.producto = []
    def agregar_producto (self, nombre, precio,ciudad):
        self.producto.append({"nombre":nombre, "precio":precio, "ciudad":ciudad})
    def total (self):
        return sum(p["precio"] for p in self.producto)
    
    def descuento(self):
        total_actual = self.total()      
        if total_actual > 300000:
            return total_actual * 0.85  
        return total_actual
    def envio(self):    
        ciudad = self.producto[0] ["ciudad"]
        if ciudad == "Popayan":
            return 0
        else:
            return 15000
    def total_final(self):
       
        return self.descuento() + self.envio()

carrito = carrito_compra()
carrito.agregar_producto("Camisa",50000, "Popayan")
carrito.agregar_producto("Pantalon",110000,"Popayan")
carrito.agregar_producto("Pantalon",150000,"Popayan")
print("Valor total: $",carrito.total())
print("Con su descuento quedaria de: $", carrito.descuento())
print("Total a pagar (con envio incluido): $", carrito.total_final())
