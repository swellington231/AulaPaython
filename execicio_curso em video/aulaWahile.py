# c = 1
# while c <=10:
#     print(c)
#     c = c + 1
# print('FIM')
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor! '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um numero: '))
    if n!=0:

        if n % 2 ==0:
            par = par +1
        else:
            impar = impar +1
print(' a Quantidade de numero PAR é {} e a quantidade de numeros Impares é {}'.format(par, impar))