from random import randint
from time import sleep
computador = randint(0,5)
print("=" * 20)
print('Vou pensar em um numero entre 0 e 5')
print("=" * 20)
jogador = int(input('Em que numero você pensou: '))
print('Processando...')
sleep(3)

if jogador == computador:
    print('PARABÉNS: Você foi o venceu')


else:
    print('Eu pensei no: {} e não {}'.format(computador, jogador) )

