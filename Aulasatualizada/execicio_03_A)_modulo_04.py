#A)
from time import sleep
try:
    soma = 0
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo numero: '))
    opção = str(input('Escolha um operador [+ - * /]: '))
    if opção == '+':
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é: {soma}')
    elif opção == '-':
        soma = n1 - n2
        print(f'A subtração de {n1} - {n2} é: {soma}')
    elif opção == '*':
        soma = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é: {soma}')

    elif opção == '/':
        soma = n1 // n2
        print(f'A divisão de {n1} * {n2} é: {soma}')
except:
    print('ERRO!')

print('Encerando Programa...')
sleep(1)
print('Obrigado... VOLTE SEMPRE')


