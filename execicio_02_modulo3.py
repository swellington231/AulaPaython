class quadrado:
        def __init__(self, tamanho_lado):
            self.tamanho_lado = tamanho_lado
        def mudar_valor_lado(self,novo_valor_lado):
                self.tamanho_lado = novo_valor_lado

        def calc_area(self):
            return self.tamanho_lado * self.tamanho_lado
        def tam_lado(self):
            return self.tamanho_lado * self.tamanho_lado / 2


soma = quadrado(17)
soma.mudar_valor_lado(5)
print(f'O calculo da area é {soma.calc_area()}')
print(f'O valor do lado é {soma.tam_lado()}')


