class Factura:
    def __init__(self, ID, vendedor, fecha_compra):
        self.factura_id = id
        self.vendedor = vendedor
        self.fecha_compra = fecha_compra

    def imprimir_info(self):
        print(f"Vendedor: {self.vendedor}")
        print(f"Fecha de compra: {self.fecha_compra}")


class DetallesFactura(Factura):
    def __init__(self, ID, vendedor, fecha_compra, producto, precio, cantidad):
        super().__init__( ID, vendedor, fecha_compra)
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.total_compra = self.calcular_total()

    def calcular_total(self):
        return self.precio * self.cantidad


if __name__ == "__main__":

   factura1 = Factura( ID=1, vendedor="jay-z", fecha_compra="2024-07-04")
   factura1.imprimir_info()

detalle1 = DetallesFactura(
    ID=1,
    vendedor="jay-z",
    fecha_compra="2024-07-04",
    producto="carro",
    precio=1000000,
    cantidad=10,
)
print(f"Producto: {detalle1.producto}")
print(f"Precio: ${detalle1.precio:.2f}")
print(f"Cantidad: {detalle1.cantidad}")
print(f"Total de compra: ${detalle1.total_compra:.2f}")