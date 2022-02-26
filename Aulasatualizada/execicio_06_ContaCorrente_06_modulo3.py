class ContaCorrente:
    def __init__(self, nome_Cliente, num_conta, saldo = 0 ):
        self.nome = nome_Cliente
        self.conta = num_conta
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self, deposito):
        self.saldo += deposito
        return self.saldo

    def saque(self, saque):
        self.saldo -= saque
        return self.saldo


n = ContaCorrente('Pedro', 1092871)
n.alterarNome('Maria Eduarda')
d = ContaCorrente('Pedro', 1092871, 500 )
s = ContaCorrente('Pedro', 1092871, 100)

print(f'Feito alteração do nome: {n.nome}')
print(f'Saldo dpoisto: {d.saldo}')
print(f'Valor do saque foi: {s.saldo}')