from  random import randint
from time import sleep
itens = (['Pedra', 'Papel', 'Tesoura'])
computador = randint(0,2)
print('''Suas opções:
       [0] PEDRA
       [1] PAPEL
       [2] TESOURA''')
jogador = int(input('Qual a sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O JOGADOR JOGOU: {}'.format(itens[jogador]))
print('O COMPUTADOR JOGOU: {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COPUTADOR GANHOU')
    else:
        print('JOGADA IVALIDA!')
if computador == 1: # COMPUTADOR JOGOU PAPEU
    if jogador == 1:
        print('DEU EMPATE!')
    elif jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
if computador == 2: # TESOURA
    if jogador == 2:
        print('DEU EMPATE!')
    elif jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVALIDA! ')
