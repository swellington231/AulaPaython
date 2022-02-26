from random import randint

computador = randint (1,10)
print('Pensei em um numero de 0 a 10: ')
print('Será que você consegue advinhar! ')
acertou = False
palpite = 0
while not acertou:
        jogador = int(input('Escolha um numero: '))
        palpite += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador > computador:
                print('Menos...Tente mais uma vez')
            elif jogador < computador:
                print('Mais...Tente mais uma vez')
print('Voce Acertou: foram {} Palpites'.format(palpite))
