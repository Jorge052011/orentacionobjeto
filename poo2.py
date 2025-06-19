# archivo orden_compra.py
from builtins import input


class OrdenCompra():
    # Se crea un método de instancia para definir atributos
    def nueva_orden(self):
        # Se define los atributos de instancia
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
        self.codigo_descuento = ""

















oc = OrdenCompra()

oc.nueva_orden()

oc.identificador = int(input("Ingrese identificador de la OC:\n"))
oc.total_productos = int(input("Ingrese total de productos:\n"))
oc.monto = int(input("Ingrese monto:\n"))


if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
    print(oc.codigo_descuento)

elif oc.monto > 10000:
    
    oc.codigo_descuento = "10PORCIENTO"
    print(oc.codigo_descuento)
