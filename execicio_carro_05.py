class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def carro_ligar(self):
        print('Carro ligou: ')
    def carro_desligar(self):
        print('Carro desligou:')
    def imprimir(self):
        print('A cor do carro é',self.cor)
        print('O modelo do carro é ', self.modelo)
        print('O ano do carro é', self.ano)


carro1 = Carro('Azul', 'Sentra', 2020)
carro2 = Carro('Preto', 'Corola', 2021)
carro3 = Carro('Cinza', 'Versa', 2020)

#Carro 01
print('Carro 1')
print()

carro1.carro_ligar()
carro1.carro_desligar()
carro1.imprimir()
print()

print('Carr0 02:')
print()
#Carro 02
carro2.carro_ligar()
carro2.carro_desligar()
carro2.imprimir()
print()
#Carro 03
print()
print('Carro 03:')
print()
carro3.carro_ligar()
carro3.carro_desligar()
carro3.imprimir()

