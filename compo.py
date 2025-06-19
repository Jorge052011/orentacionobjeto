
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
Esto sería una herencia ereda la clase moto, hay que compararlo con el metodo anterior de composicion
class Auto(Motor):
    def __init__(self, marca):
        self.marca =marca
       

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

