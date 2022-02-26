# Execicio imprimir por extenso em uma tupla

# extenso = ('zero', 'um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatoze',
#           'Quize','Dezeceis','Dezessete','Dezoito','Dezenove','Vinte')
# while True:
#     num = int(input('Digite um numero: '))
#     if 0 <= num <=20:
#         break
# print(f'O numero digitado foi : {extenso[num]}')

#Ciar uma tupla para tabela do brasileiro

# brasileiro = ('Palmeiras','Flamengo','Chapecoense','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos'
#                 'Bahia','Fluminense','Corinthians','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
# print('='*40)
# print(f'A) Os primeiro cinco colocados são: {brasileiro[:5]}')
# print(f'B) Os ultimos quatro colocados são: {brasileiro[-4:]}')
# print(f'C) Times em ordem alfabetica: {sorted(brasileiro)}')
# print(f'O chapecoence esta na {brasileiro.index("Chapecoense")+1}ª posição')

# Programa que imprima uma listagem aleatorio

# from random import randint
# num = randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9)
# for n in num:
#     print(n, end=' ')
# print(f'\nO maior numero é {max(num)}')
# print(f'O menor numero é: {min(num)}')

# Adcionar numeros aleatorios em uma Tupla.
# num = (int(input('Digite um numero:')),
#        int(input('Digite mais um numero: ')),
#        int(input('Digite o terceiro numero: ')),
#        int(input('Digite o ultimo numero: ')))
# print(f'A) O numero 9 apareceu {num.count(9)} vez')
# if num == 3:
#     print(f'B) O numero 3 apareceu {num.count(3)} vezes')
# else:
#     print('O numero 3 não foi digitado: ')
#     print('Os numero Pares são: ')
# for n in num:
#     if n % 2 ==0:
#         print(f'{n}',end=' ')

#Lista de preço com tupla

listagem =('Lapis', 2, 'Borracha', 3 ,'Caderno', 15, 'Lapizeira', 4.50 ,'Garrafa', 14 ,'Caneta', 3.59,'Estojo', 7.50 , 'Livro', 35 )

print('-'*40)
print('LISTAGEM DE MATERIAL')
print('-'* 40)
for pos in range(0, len(listagem)):
   if pos % 2 == 0:
       print(f'{listagem[pos]:.<30}',end='')
   else:
       print(f'R${listagem[pos]:>6.2f}')

