dad1 = []
pricip = []
mai = men = 0
while True:
    dad1.append(str(input('Nome: ')))
    dad1.append(float(input('Peso: ')))
    if len(pricip) == 0:
        mai = men = dad1[1]
    else:
        if dad1[1] > mai:
            mai = dad1[1]
        if dad1[1] < men:
            men = dad1[1]

    pricip.append(dad1[:])
    dad1.clear()

    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(pricip)} Pessoas : ')
print(f'{mai} Kg o Maior peso foi: ', end=' ')
for p in pricip:
  if p[1] == mai:
      print(f'[{p[0]}]', end=' ')
print()
print(f'\n {men} Kg O menor peso é de: ',end='' )
for p in pricip:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()