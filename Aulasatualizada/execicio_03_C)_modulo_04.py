def mult():
    try:
        n1 = int(input('Digite primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        s = n1 * n2
        print(f'A multiplicação dos numero é: {s}')
    except (ValueError, TypeError):
        print('Digite um numero Valido:')
    finally:
        print('Obrigado! Volte sempre! ')

mult()