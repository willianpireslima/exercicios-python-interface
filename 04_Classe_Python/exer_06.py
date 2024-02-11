class Derivada:
    def __init__(self, auxCA, auxCB, auxCC):
        self.CA = auxCA
        self.CB = auxCB
        self.CC = auxCC

    def derivar(self):
        xi = -self.CB / (2 * self.CA)
        deriv = 2 * self.CA * xi + 2
        equacao = self.CA * (deriv * deriv) + self.CB * deriv + self.CC

        return equacao

    def eixoXandY(self, X, Y):
        limiteX = X / 2
        limiteY = Y / 2
        Tamanho = int(self.derivar())

        VetorX = []
        VetorY = []

        for i in range(int(-limiteX), int(limiteX) + 1, 1):
            VetorX.append(i)

        for i in range(int(-limiteY), int(limiteY) + 1, 1):
            VetorY.append(i)

        print("Vetor X")
        for i in range(0, len(VetorX), 1):
            print(VetorX[i])

        print("Vetor Y")
        for i in range(0, len(VetorY), 1):
            print(VetorY[i])


obj = Derivada(4, 6, 3)
print(f" Derivada {obj.derivar()}")
obj.eixoXandY(3, 8)

