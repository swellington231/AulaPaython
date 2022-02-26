tot = 0
num = int(input('Digite um numero: '))
for c in range (1, num + 1):

    if num % c == 0:
        print("\033[34m",end=" ")
        tot += 1

    else:
        print("\033[31m",end=' ')
    print(' {} '.format(c), end=' ')
print('O numero {} é divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('O numero {} dividiu {} vezes ele é PRIMO'.format(num, tot))
else:
    print('O numero {} divide por {} por isso não é PRIMO'.format(num, tot))

