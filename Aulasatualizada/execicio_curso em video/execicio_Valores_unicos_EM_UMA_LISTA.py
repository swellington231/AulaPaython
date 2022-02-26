listnum = []
while True:
    num = int(input('Digite um numero: '))
    if num not in listnum:
        listnum.append(num)
        print('Numero adcionado...')
    else:
        print('Numero duplicado.. não pode ser adcionado: ')

    opção =' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? S/N: ')).strip().upper()
    if opção == 'N':
        break
print(f'Os numeros digitados foram {listnum}')