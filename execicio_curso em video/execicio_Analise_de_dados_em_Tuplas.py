num = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: ')))
print(f'Os numero digitados foram: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'\nO numero 3 foi digita a primeira vez na posição: {num.index(3)+1}ª')
else:
    print('O valor três não foi digitado: ')
print('Os numeros pares são: ')
for n in num:
    if n % 2 == 0:
        print(f'{n}',end= ' ')

