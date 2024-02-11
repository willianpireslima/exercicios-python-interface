class Fracao:
    def __init__(self, auxnumA, auxdenA, auxnumB, auxdenB):
        self.numA = auxnumA
        self.denA = auxdenA
        self.numB = auxnumB
        self.denB = auxdenB
    def getNum(self):
        return self.resuNum

    def getDen(self):
        return self.resulDen

    def mdc(self, Valor1, Valor2):
        while Valor2 != 0:
            Valor1, Valor2 = Valor2, Valor1 % Valor2
        return Valor1

    def soma(self):
        denSom = self.denA * self.denB
        numSom = self.numA * self.denB + self.numB * self.denA
        storeMdc = self.mdc(numSom, denSom)
        if storeMdc != 0:
            self.resuNum = numSom // storeMdc
            self.resulDen = denSom // storeMdc
        else:
            self.resuNum = 0
            self.resulDen = 0
            print("Impossível calcular a soma. MDC é zero.")

    def subb(self):
        denSub = self.denA * self.denB
        numSub = self.numA * self.denB - self.numB * self.denA
        storeMdc = self.mdc(numSub, denSub)
        if storeMdc != 0:
            self.resuNum = numSub // storeMdc
            self.resulDen = denSub // storeMdc
        else:
            self.resuNum = 0
            self.resulDen = 0
            print("Impossível calcular a subtração. MDC é zero.")

    def multi(self):
        numMul = self.denA * self.denB
        denMul = self.numA * self.numB
        storeMdc = self.mdc(numMul, denMul)
        if storeMdc != 0:
            self.resuNum = denMul // storeMdc
            self.resulDen = numMul // storeMdc
        else:
            self.resuNum = 0
            self.resulDen = 0
            print("Impossível calcular a multiplicação. MDC é zero.")

    def divis(self):
        numDiv = self.denA * self.numB
        denDiv = self.numA * self.denB
        storeMdc = self.mdc(denDiv, numDiv)
        if storeMdc != 0:
            self.resuNum = denDiv // storeMdc
            self.resulDen = numDiv // storeMdc
        else:
            self.resuNum = 0
            self.resulDen = 0
            print("Impossível calcular a divisão. MDC é zero.")


obj = Fracao(1, 3,5,5)
obj .soma()
print(obj.getNum(), "/", obj.getDen())


