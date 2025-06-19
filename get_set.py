
   

class Dato:
    def __init__(self,dato):
        self.dato = dato 

    def __str__(self):
        return f"{self.dato}"
    

    def __add__(self, inst):
        return Dato(self.dato + inst.dato)
    

    def __sub__(self, otro_self):
        return Dato(self.dato - otro_self.dato)
    




dato1 = Dato(112)
dato2 = Dato(100)

dato1 + dato2 #invoca dato1.__add__(dato2)
resultado_resta = dato1 - dato2
print(resultado_resta)


class Dato2(Dato):
    def __init__(self, dato, numero):
        super().__init__(dato)
        self.numero = numero


    def __str__(self):
        print("askjldhsal")



    
        