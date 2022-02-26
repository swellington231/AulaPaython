class Bola:
    def __init__(self, cor,circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    def mostraCor(self):
        return self.cor

bola = Bola('Verde', '7', 'Borracha')
bola.trocaCor('Preta')
print(bola.mostraCor())
