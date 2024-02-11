import math

class Triangulo:

    def __init__(self,auxA,auxB,auxC):
        self.a = auxA
        self.b = auxB
        self.c = auxC

    def mostrarLados (self):
        print(f"Lado 1 : {self.a} Lado 2 : {self.b} Lado 3 : {self.c}")

    def classificarTipo(self):
        if self.a == self.b and  self.b == self.c and  self.c == self.a:
            return "Triangulo Equilatero"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Isosceleso"
        elif self.a != self.b and  self.b != self.c and self.c != self.a:
            return "Escaleno"

    def classificarLado (self):

        if self.a * self.a < self.b * self.b + self.c * self.c:
            return "Acutangulo"
        elif self.a * self.a > self.b * self.b + self.c * self.c:
            return "Obtusangulo"
        elif self.a * self.a == self.b * self.b + self.c * self.c:
            return "Retangulo"


obj = Triangulo (3,10,5)
obj.mostrarLados()
print(obj.classificarTipo())
print(obj.classificarLado())
