from random import randint
while True:
    dado = randint(1,6)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de Jogar o DADO? [S/N?]')).strip().upper()[0]
    if resp == 'N':
        break
    if resp == 'S':
        print(f'O Resultado foi {dado}')


print('FIM DE JOGO')