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

carros = []

while True: 
    marca = input("insira a marca do carro ou 'sair' para encerrar o programa:")

    if marca.lower() == "sair":
        break
    
    modelo = input("Insira o modelo do seu carro:")

    cor = input("Insira a cor do seu carro:")

    ano = input("Insira o ano do seu carro:")

    carro = Carro(marca, modelo, cor, ano)
    carros.append(carro)

print("\n Informações dos carros: ")

for i, carro in enumerate(carros, start=1):
    print(f"\n Carro {i}")
    carro.exibir_informacoes()

input()