from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
            'Jogador2': randint(1,6),
            'Jogador3': randint(1,6),
            'Jogador4': randint(1,6)}
ranking = list()
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado ')
    sleep(1)
rankig = sorted(jogo.items(), key=itemgetter(1))
print(rankig)
for i,v in enumerate(rankig):
    print(f'{i+1}º Lugar  {v[0]} com {v[1]} ')