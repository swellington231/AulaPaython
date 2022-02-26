preço = float(input('Informe o preço do produto: '))
print('''Escolha uma opção de pagamento:
        [1] A vista no DINHEIRO / CHEQUE
        [2] A vista no CARTÂO
        [3] 2X no CARTÂO
        [4] 3X no CARTÂO''')
opção = int(input('Escolha a opção: '))

if opção == 1:
    desconto = (preço * 10)/100
    novo_preço = preço - desconto
    print('O preço do produto é R$ {:.2f} com desconto ficou em R$ {:.2f} '.format(preço,novo_preço))

elif opção == 2:
    desconto = (preço * 5 )/ 100
    novo_preço = preço - desconto
    print('O preço do produto é R$ {:.2f} com desconto ficou {:.2f} '.format(preço,novo_preço))
elif opção == 3 :
    parcela = preço / 2
    print('O preço do produto é R$ {:.2f} com  PAGAMENTO é em 2X de R$ {:.2f}'.format(preço, parcela))
elif opção == 4:
    juros = (preço * 20)/100
    novo_preço = (preço + juros)
    parcela = novo_preço / 3
    print('O predo do produto é {} em 3X o valor da parcela é {} no total de {}'.format(preço, parcela, novo_preço))
