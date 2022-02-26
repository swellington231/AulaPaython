from random import randint
v = 0
while True:
    jogador = int(input('Escolha um numero: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Escolha PAR ou IMPAR [P/I]')).strip().upper()
    print(f'O Jogador jogou {jogador} e o computador {computador} e o total foi {total} ')
    if tipo == 'P':
        if total % 2 == 0:
                print('VOCÊ VENCEU!')
                v += 1
        else:
                print('VOCÊ PERDEU')
                break

    elif tipo == 'I':
        if total % 2 == 1:
                print('VOCÊ VENCEU')
                v +=1
        else:
                print('VOCE PERDEU')
                break
        print('Vamos jogar novamente... ')
print(f'THAU. Você teve {v} VITORIAS ')


