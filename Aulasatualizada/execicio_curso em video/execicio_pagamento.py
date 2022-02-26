preço = float(input('Digite o valor do produto: R$'))
pgto = float(input('Escolha a forma de pagamento'
              '[1] A dinheiro com 10% de DESCONTO'
              '[2] Cartão de debito com 5% de DESCONTO'
              '[3] Cartão de credito com 8% de AUMENTO'))

novo_preço = preço - (preço * 10 / 100)

if pgto == '1':
    novo_preço = preço - (preço * 10 / 100)
print('O preço do produto é {} com pagamento em dinheiro  ficou {} R$  com 5% de desconto'.format(preço, novo_preço))

elif pgto == '2':
    novo_preço = preço - (preço * 5 / 100)
print(' O preço do produto é {} com Pgto em cartão de debito R$ {} com 5% de desconto'.format(preço, novo_preço))

elif pgto == '3':
    novo_preço = preço + (preço * 8 / 100)
print('O preço do produto é {} com Pgto no cartão de credito ficou {} com *% de aumento'.format(preço, novo_preço))
