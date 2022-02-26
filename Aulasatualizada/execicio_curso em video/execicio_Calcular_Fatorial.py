# from math import factorial
# print('Digite um numero:')
# numero = int(input('Calcular o Fatorial: '))
# f = factorial(numero)
# print('O fatorial de {} é {}'.format(numero, f))
n = int(input('Digite o numro pra calcular o FATORIAL: '))
c = n
f = 1
print('{}! = '.format(n),end= " ")
while c > 0:
    print('{}'.format(c),end=" ")
    f = f * c
    c -=1
    print('X'if c >=1 else '=', end=" ")
print('{}'.format(f),end=" ")

