import math
class Cone:

    def __init__(self,auxRaio,auxAltura):
        self.raio =auxRaio
        self.altura = auxAltura

    def mostrarRaio (self):
        return self.raio

    def mostrarAltura (self):
        return self.altura

    def mostrarGeratriz (self):
        return math.sqrt(self.altura*self.altura)+(self.raio*self.raio)

    def mostrararArealateral (self):
        return 3.14*self.raio*self.raio*self.mostrarGeratriz()

    def mostrararAreaTotal(self):
        return 3.14*self.raio*(self.mostrarGeratriz() + self.raio)



obj = Cone (3.0,10.0)
print(f"Raio : {obj.mostrarRaio()}")
print(f"Altura : {obj.mostrarAltura()}")
print(f"Geratriz : {obj.mostrarGeratriz()}")
print(f"Area lateral {obj.mostrararArealateral():.2f} ")
print(f"Area Total {obj.mostrararAreaTotal()}")