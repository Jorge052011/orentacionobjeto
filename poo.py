from abc import ABC



class Menu: 
    def __init__(self, opciones):
        self.__marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar(self):
            print(self.get_marca(), self.modelo, self.anio, self.puertas)


    def get_marca(self) -> str:
            return self.__marca

    def set_marca(self, nueva_marca: str) -> None:
            self.__marca = nueva_marca


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas,password):
        super().__init__(marca, modelo, anio)

        self.puertas =  puertas
        self.tipo_motor = "lc8"
        self.password = "1234"
        self.password = password
    @property
    def get_puertas(self):
        return self.puertas
    
    def set_puertas(self,puerta):
        self.puertas = puerta

    def mostrar(self):
           return self.get_marca(), self.modelo, self.anio, self.puertas

    
    
auto_1 = Auto("toyota","corola",2022 ,4)


auto_1.set_marca("hola")
print(auto_1.get_puertas)





