pessoa = dict()
qtdePessoas = list()
soma = media = qtdeMulher = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F')
    pessoa['idade'] = float(input('Idade: '))
    soma += pessoa["idade"]
    qtdePessoas.append(pessoa.copy())
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continur [S/N]?')).strip().upper()
    if opção == 'N':
        break
media = soma / len(qtdePessoas)
print(f'A) Foram cadastradas {len(qtdePessoas)} Pessoas')
print(f'B) Á media de idade é {media:.1f}')
print('C) As mulheres cadastradas são.')
for n in qtdePessoas:
    if n['sexo'] in 'Ff':
        print(f' {n["nome"]}')
print()
print('D) As pessoas acima da média são:')
for p in qtdePessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k}  = {v}', end='')
            print()