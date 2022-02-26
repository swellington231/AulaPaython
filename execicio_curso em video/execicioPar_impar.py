numero = int(input('Digite um numero interio: '))
resultado = numero % 2
if numero % 2 == 0:
    print('O numero {} é PAR '.format(numero))
else:
    print('O numero {} é IMPAR '.format(numero))