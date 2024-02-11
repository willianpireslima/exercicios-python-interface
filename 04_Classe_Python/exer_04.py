
class Estoque:

    def __init__(self,auxDescric,auxProdNum,auxQde,auxPreco):
        self.descric = auxDescric
        self.prodNum = auxProdNum
        self.qde = auxQde
        self.preco = auxPreco

    def get (self):
        print(f"{self.descric} {self.prodNum} {self.qde} {self.qde}")

obj = []
obj.append(Estoque("Pao",1,5,8.9))
obj.append(Estoque("Manteiga",2,59,6.9))
obj.append(Estoque("Cafe",3,87,7.4))
obj.append(Estoque("Leite",4,45,7.6))
obj.append(Estoque("Cadeira",34,5,1.2))
obj.append(Estoque("Mesa",6,12,5.6))
obj.append(Estoque("Comp",7,89,9.5))
obj.append(Estoque("Sofa",8,43,8.1))
obj.append(Estoque("Geleia",9,35,5.4))
obj.append(Estoque("Bailinha",10,76,4.5))
obj.append(Estoque("Chocolatw",11,30,7.5))

for i in range (0,10,1):
     obj[i].get()