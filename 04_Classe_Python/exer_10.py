class Forca:
    def __init__(self):
        self.palavra = ""
        self.resul_verif = ""
        self.vencedor = 0
        self.perdedor = 0

    def set_palavra(self, aux):
        self.palavra = aux

    def get_palavra(self):
        return self.palavra

    def get_resul_verif(self):
        return self.resul_verif

    def verificar(self, letra):
        posicao = self.palavra.find(letra)
        if posicao != -1:
            self.vencedor += 1
            self.resul_verif = f"Caractere {letra} em {posicao}\n" \
                                f"Letras Acertadas: {self.vencedor}\n" \
                                f"Letras Erradas: {self.perdedor}"
        else:
            self.perdedor += 1
            self.resul_verif = f"Nao Encontrado\n" \
                                f"Letras Acertadas: {self.vencedor}\n" \
                                f"Letras Erradas: {self.perdedor}"


# Exemplo de uso
forca = Forca()
forca.set_palavra("python")
forca.verificar("p")
print(forca.get_resul_verif())
