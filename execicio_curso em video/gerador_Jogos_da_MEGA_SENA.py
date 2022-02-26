from random import randint
from time import sleep
cont = 1
lista = []
jogos = []
tot =1
quant = int(input('Quantos jogos você quer? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('='*4 ,f'SORTEANDO {quant} Jogos')
print('Gerando Jogos... ')
sleep(2)
for i, v in enumerate (jogos):
    print(f'{i+1}º Jogo: {v}')
    sleep(3)


