maiorIdade = qtdehome = mulher = 0
while True:
    idade = int(input(' idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(' SEXO [MF]: ')).upper().strip()[0]
    opção = ' '
    while opção not  in 'SN':
        opção = str(input('Quer continuar S/N')).strip().upper()[0]
    if opção == 'N':
        break
    if idade >=18:
        maiorIdade += 1
    if sexo == 'M':
        qtdehome += 1
    if sexo in 'F' and idade > 20:
        mulher += 1

print(f'são  {maiorIdade} pessoas mair de 18 anos são {qtdehome} homes e {mulher} mulher maior  de 20 anos')

print('FIM')
