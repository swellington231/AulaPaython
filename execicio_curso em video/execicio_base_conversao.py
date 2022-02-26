n = int(input('Digite um numero: '))
print('''Escolha uma opção de coversão:'
              [1] Para BINARIO
              [2] Para OCTAL
              [3] Converter para EXADECIMAL''')
opcao = int(input('Escolha uma opção:'))

if opcao == 1:

    print('{} converteido em BINARIO É {}'.format(n, bin(n)[2:]))

elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(n, bin(n)[2:]))

elif opcao == 3:
    print('{} Convertido em EXABECIMAL é {}'.format(n, bin(n)[2:]))

else:
    print('Opção invalida tente novamente!')