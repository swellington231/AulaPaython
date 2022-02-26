pessoa = dict()
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    sexo = ' '
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Escolha M ou F: ')
    try:
        pessoa['idade'] = int(input('Idade: '))
    except (ValueError, TypeError):
        print('Por favor digitar um numero inteiro Valido: ')
        continue

    soma += pessoa['idade']
    galera.append(pessoa.copy())
    opção = ' '
    while opção not  in'SN':
        opção = str(input('Deseja continumar [S/N]')).strip().upper()[0]
    if opção in 'N':
            break
print(f'A) Foram cadastradas {len(galera)} Pessoas')
media = soma / len(galera)
print(f'B) A média de idade é {media:.2f} anos')

print('C) As mulheres cadastras são: ')
for m in galera:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]}', end='')
    print()
print('D) Lista das pesoas que estão acima da média: ')
for p in galera:
    if p['idade']>= media:
        for k, v in p.items():
            print(f'{k} = {v}')
        print()