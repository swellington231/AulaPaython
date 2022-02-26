from time import sleep
n1 = int(input('Digite o primerio numero: '))
n2 = int(input('Digite o segundo numero: '))
opção = 0
r = 0
maior = 0

while opção !=5:
    print('''Opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do Programa''')
    opção = int(input('Escolha uma opção: '))
    if opção == 1 :
        r = n1 + n2
        print('O valor da soma é {} '.format(r))
    elif opção == 2:
        r = n1 * n2
        print('O valor da multiplicação é {}'.format(r))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero é {}'.format(maior))
        else:
            maior = n2
            print('O numero maior é {} '.format(maior))
    elif opção == 4:
        print('Informe os numro outra vez: ')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    else:
        print('Opção invalida! Tente outra vez ')

print('Finalizando...')
sleep(1)
print('Programa finalizado!')
