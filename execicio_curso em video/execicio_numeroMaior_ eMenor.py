
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo Numero: '))
c = int(input('Digite o terceiro numero: '))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c > a and c < b:
    menor = c

if a > b and a > b:
    maior = a
elif b > a and b > c :
    maior = b
elif c > a and c > b:
    maior = c

print('O maior numero é {} '.format( menor ))
print('O maior foi {} '.format(maior))

