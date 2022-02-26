from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os numero Sorteado foram: ')
for n in num:
    print(f' {n}', end=' ')
print(f'\nO maior numero é {max(num)}')
print(f'O menor numero é {min(num)}')