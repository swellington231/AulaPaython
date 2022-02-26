lista = []
media = 0
soma = 0
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2) /2
    lista.append([nome, [n1, n2], media])
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continura? [S/N]? ')).strip().upper()
    if r == 'N':
        break
for i, n in enumerate(lista):
    print(f'{i+1:<4}{n[0]:<10}{n[2]:<8.1f}')
while True:
    opc = int(input('Qual aluno você quer ver a nota [999 interrope o programa]: '))
    if opc == 999:
        break
    if opc == len(lista) - 1:
        print(f'{lista[opc][0]} e as notas são {lista[opc][1]}')
