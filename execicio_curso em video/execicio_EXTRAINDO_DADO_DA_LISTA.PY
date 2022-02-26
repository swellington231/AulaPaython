listnum = []
cont = 0
while True:
    n = int(input('Digite um numero: '))
    listnum.append(n)
    listnum.sort(reverse= True)
    cont = cont + 1
    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar S/N?' ).strip().upper()
    if r == 'N':
        break

print(f'Foram digitados {cont} valores')
if n == 5:
    print(f'O numero {n} foi digitado: ')
else:
    print('O numro 5 não foi digitado ')
print(f'Lista em ordem decrescente {listnum}')

