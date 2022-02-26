from random import randint
while True:
    try:
        computador = randint(1,10)
        print('Vou pensar em um numero em 0 e 10')
        print('='* 20)
        jogador = int(input('Pense em um numero: '))
        if computador == jogador:
            print(f'O computador jogou {computador} e você jogou em {jogador} PARABÉNS VOCÊ ACERTOU')
        else:
            print(f'O computador jogou {computador} e o você Jogou {jogador} ERROU')
        if jogador > computador:
            print('Menos...')
        elif jogador < computador:
            print('Mais...')

    except:
        print('ERRO! Digite um numero inteiro')
        break

