class BombaCombustivel():
    def __init__(self,tip_combustivel, valor_litro:float, qtde_combuistivel:float):
        self.tip_combustivel = tip_combustivel
        self.valor_litro = valor_litro
        self.qtde_combustivel = qtde_combuistivel

    def abatecerPorValor(self, valor:float):
        litros_abatecido = valor / self.valor_litro
        self.qtde_combustivel -= litros_abatecido
        print(f'A quantidade de litros abastecido foi {litros_abatecido:.2f} Litros.')
        print(f'Restaram {self.qtde_combustivel:.2f} na bomba')

    def abatecerPorLitro(self, litro_abastecido:float):
        valor  = litro_abastecido * self.valor_litro
        self.qtde_combustivel -= litro_abastecido
        print(f'O valor a ser pago é R$ {valor:.2f}')
        print(f'Restam {self.qtde_combustivel:.2f} na Bomba')

    def alterarPreco(self, novo_preco:float):
        self.valor_litro = novo_preco
        print(f'O novo valor do litro é R$ {novo_preco:.2f}')

    def alterarCombustive(self, novoCombustivel:str):
        self.tip_combustivel = novoCombustivel
        print(f'Você está abastecendo com {self.tip_combustivel}')

    def alterarQuantidadeCombustivel_naBomba(self, novaQtdeCombustivel:float):
        self.qtde_combustivel = novaQtdeCombustivel
        print(f'Atualazado  quantidade de combustivel da bomba {novaQtdeCombustivel}')

abt = BombaCombustivel('Gasolina', 6.00, 100)
abt.alterarPreco(6.10)
abt.abatecerPorValor(60)
abt.abatecerPorLitro(10)
abt.alterarPreco(7.10)
abt.alterarCombustive('Etanol')
abt.alterarQuantidadeCombustivel_naBomba(5000)
abt.abatecerPorValor(60)
