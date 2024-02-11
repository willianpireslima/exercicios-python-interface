class Contatos:
    def __init__(self, auxNumer):
        self.number = auxNumer

    def getNumber(self):
        return self.number

class Agenda:
    def __init__(self):
        self.ContatosLista = []
        self.indice = 0

    def setContato(self, auxNumero):
        self.ContatosLista.append(Contatos(auxNumero))
        self.indice += 1
        print("Contato Inserido")

    def getContato(self):
        for contato in self.ContatosLista:
            print(contato.getNumber())

    def buscarContato(self, aux):
        for contato in self.ContatosLista:
            if contato.getNumber() == aux:
                return "Contato Encontrado"
        return "Contato Não Encontrado"

    def modificarContato(self, oldContato, newContato):
        for i, contato in enumerate(self.ContatosLista):
            if contato.getNumber() == oldContato:
                self.ContatosLista[i] = Contatos(newContato)
                return "Contato Modificado"
        return "Contato Não Encontrado"

    def excluirContato(self, auxExc):
        for i, contato in enumerate(self.ContatosLista):
            if contato.getNumber() == auxExc:
                del self.ContatosLista[i]
                self.indice -= 1
                return "Contato Excluído"
        return "Contato Não Encontrado"

# Testando o código
obj = Agenda()
obj.setContato(9)
obj.setContato(3)
obj.setContato(4)
obj.getContato()
print(obj.buscarContato(9))
print(obj.modificarContato(9, 4))
print(obj.excluirContato(3))
obj.getContato()
