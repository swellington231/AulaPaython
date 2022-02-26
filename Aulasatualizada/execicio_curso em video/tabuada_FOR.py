r = 0
n = int(input('Digite um numero para multiplicar: '))
for c in range (1,11):
    r = c * n
    print('{}  X {} = {}'.format(n, c, r))
