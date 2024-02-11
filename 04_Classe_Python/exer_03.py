import math

class Equa2Grau:

    def __init__(self,auxA,auxB,auxC):
        self.a = auxA
        self.b = auxB
        self.c = auxC
        self.delta = auxB*auxB - 4*auxA*auxC

    def CalcularRaizes (self):
        if self.delta > 0 :
            x1 = (-self.b + math.sqrt(self.delta))/(2 * self.a)
            x2 = (-self.b - math.sqrt(self.delta))/(2 * self.a)
            print(f"Duas Raizes x1 : {x1:.2f} x2 {x2:.2f}")
        elif self.delta == 0 :
            x1 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            print(f"Raizes Unica x1 : {x1:.2f}")
        elif self.delta < 0:
            print(f"Raizes imaginarias")

obj = Equa2Grau (3,40,  7)
obj.CalcularRaizes()