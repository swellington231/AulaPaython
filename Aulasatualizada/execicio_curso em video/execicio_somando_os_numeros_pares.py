somaPar = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        somaPar = somaPar + n
        cont = cont + 1

print('Você informou {} PARES a a soma dos numeros  são {} : '.format(cont, somaPar))






