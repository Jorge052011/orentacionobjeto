

from builtins import print


class Medicamento:
    descuento = 0.05
    IVA = 0.18
    def __init__(self,nombre, stock):
        self.nombre = nombre
        self.stock = stock
    @staticmethod
    def validar_mayor_a_0(numero):
        return numero > 0 
    
    def asigna_precio(self, precio):
        es_valido = self.validar_mayor_a_0(precio)
        if es_valido:
            self.precio = precio
            self.descuento = 0.0
            
            if self.precio >= 10000 and self.precio < 20000:
                self.descuento = 0.1
            elif self.precio >= 20000 and self.precio < 30000:
                self.descuento = 0.2
            elif self.precio >= 30000:
                self.descuento = 0.3
            print(self.descuento)
        else:
            print("no es valido")

    def __eq__(self, otra):
        return self.nombre == otra.nombre
        

    def __iadd__(self, otra):
        if self == otra:
            self.stock += otra.stock
        return self
    
    def __str__(self):
        return f"el medicamento {self.nombre} tiene: {self.stock} stock"


aspirina = Medicamento("a", 10)
paracetamol = Medicamento("a", 10)
aspirina2 = Medicamento("a", 2)



aspirina += aspirina2
print(aspirina)

















