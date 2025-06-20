"""
class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f"{self.nombre}"


class Hospital:
    def __init__(self, nombre):
       self.nombre = nombre
       self.pacientes = []


    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def __str__(self):
        return f"{self.nombre}"


paciente = Paciente("Juan")
hospital =Hospital("Hospital dr simi")
print(hospital)
## AGREGACION por que las dos clase no dependen fuertemente ( se graga el objeto paciente, pero tambien se llama composición debil)
hospital.agregar_paciente(paciente)



## COMPOSICION
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        pass

class Auto:
    def __init__(self, marca):
        self.marca =marca
        self.motorcito = Motor("4v")

"""
"""
Esto sería una herencia ereda la clase moto, hay que compararlo con el metodo anterior de composicion
class Auto(Motor):
    def __init__(self, marca):
        self.marca =marca
       
"""
"""
class Bateria:
    def __init__(self, cap):
        self.cap =cap

class Pantalla:
    def __init__(self, tamanio):
        self.tamanio = tamanio

class Telefono:
    def __init__(self, modelo):
        self.modelo = modelo
        self.bateria = Bateria ("5000mh")
        self.pantalla = Pantalla("FULLDH")

    def __str__(self):
        return f"{self.modelo}----{self.bateria}----{self.pantalla}"
    
s21 = Telefono("s21")
print(s21)

####interfase de una tienda
from abc import ABC, abstractmethod
class Tienda(ABC):

    @abstractmethod
    def vender():
        pass
    @abstractmethod
    def comprar():
        pass

class Tienda_de_ropa(Tienda):
    @abstractmethod
    def vender():
        pass
    @abstractmethod
    def comprar():
        pass


class Tienda_de_deportes(Tienda):
    @abstractmethod
    def vender():
        pass
    @abstractmethod
    def comprar():
        pass

class Tienda_de_zapatos(Tienda):
    @abstractmethod
    def vender():
        pass
    @abstractmethod
    def comprar():
        pass




"""
"""
from abc import ABC, abstractmethod

class SinGluten():
    tipo_producto = "sin gluten"





class Chocolate(ABC):

    def __init__(self, porc_cacao):
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)

    @abstractmethod
    def validar_porc_cacao(self,porc):
        pass

class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc):
        return min(max(0.75, porc),0,85)
    
class Chocman(ChocolateAmargo, SinGluten):
    pass

c= ChocolateAmargo(0.3)
print(c.porc_cacao)

print(Chocman.__mro__)
    
"""
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def mostrar_info(self):
        print(f"tienda : {self.nombre} - direccion : {self.direccion}")

    @abstractmethod
    def vender(self, producto):
        pass

    @abstractmethod
    def facturar(self):
        pass

class Tienda_ropa(Tienda):
    def vender(self, producto):
        print(f"vendiendo un {producto}")

    def facturar(self):
        print("facturandooo")


class Tienda_electronica(Tienda):
    def vender(self, producto):
        print(f"vendiendo un {producto}")

t = Tienda_ropa("ABCDIN","caklle falsa 123")

t.vender("pantalon")
t.facturar()


te = Tienda_electronica("ABCDIN","caklle falsa 123")

te.vender("memoria ram")  ####revisar en video falto algo












