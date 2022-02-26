galera = list()
pessoa = dict()

while True:
    pessoa['nome'] = str (input('Nome: ')).capitalize()

    while True:
        pessoa['sexo'] = str(input('Sexo M/F: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR! Digite  M ou F!:')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar S/N: ')).upper()[0]
        if resp in 'SN':
            break
            print('ERRO! Escolha S ou N:')
    if resp == 'N':
        break

print(f'Ao todos temos {len(galera)} pessoas cadastradas')
media = soma /len(galera)
print(f'A media da Idade {media.5.2f}anos')