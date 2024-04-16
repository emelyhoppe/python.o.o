class Carro:
    def __init__(self,marca,modelo,cor,ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

def exibir_informacoes(self):
    print("Marca: ", self.marca)
    print("Modelo: ", self.modelo)
    print("Cor: ", self.cor)
    print("Ano: ", self.ano)

carro1 = Carro("Toyota, Corolla, Prata", 2002)
carro2 = Carro("Hoonigan, Hoonicorn, Cinza", 1965)
carro3 = Carro("Ford, Mustang, Vermelho", 1969)

carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()

input()