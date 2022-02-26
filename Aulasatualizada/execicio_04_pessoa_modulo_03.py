class pessoa:


    def __init__(self, nome, idade, peso, altura:float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def envelhecer(self,anos):
        self.idade = self.idade + anos
        print(f'Sua idade atual é {p.idade} anos')

    def engordar(self, kg):
        self.peso += kg
        print(f'Você emgordou e está com  {p.peso} KG')

    def emagrecer(self, perder_peso):
        self.peso -= perder_peso
        print(f'Você emagreceu e está com {p.peso} Kg')

    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.5
            print(f'Você está com {p.altura} altura')
        else:
            print('Você já é maior de 21 anos ')


p = pessoa('Paulo', 18, 86, 1.70)
p.engordar(10)
p.emagrecer(20)
p.envelhecer(3)
p.crescer()
