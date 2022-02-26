num = list()
numPar = []
numImpar =[]

while True:
    n = int(input('Digite um numero: '))
    num.append(n)
    if n % 2 == 0:
        numPar.append(n)
    else:
        numImpar.append(n)

    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar S/N? ').strip().upper()
    if r == 'N':
        break
print(f'Os numeros digitados foram: {num}')
print(f'Os numero pares são {numPar}')
print(f'Os numeros impares são {numImpar}')
