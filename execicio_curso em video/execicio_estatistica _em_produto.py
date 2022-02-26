total = preçoMil = preço = menor = produto = contar = 0
barato = ' '
while True:
    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preço = float(input('Digite o preço: '))
    contar += 1
    total += preço
    if preço > 1000:
        preçoMil += 1
    if contar == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar... S/N? ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'O valor Total de compra foi {total:.2f}')
print(f'Foram {preçoMil} maior que MIL Reais. ')
print(f'O menor preço foi {barato} e o menor preço foi  {menor:.2f} ')
print('ACABOU')

