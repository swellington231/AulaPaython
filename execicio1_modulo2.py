galera = list()
pessoa = dict()
soma = idade = 0
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite M ou F' )
    pessoa['idade'] = int(input('Idade'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: S/N')).upper()[0]
        if  resp in 'SN':
            break
        print('ERRO! Escolha apenas S ou N.')
    if resp == 'N':
            break
print('-=' * 30)
print(f'A) Ao todos temos {len(galera)} pessoa cadastradas')
media = soma / len(galera)
print(f'B) a media de idade é {media:5.2f}anos')
for p in galera:
    if  p['sexo']  in 'Ff':
        print(f'C) {p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p ['idade']>= media:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ' , end='')
            print()
print('<<ENCERRADO>>')
