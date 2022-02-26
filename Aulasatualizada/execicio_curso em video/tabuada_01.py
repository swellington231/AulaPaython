aux = 0
valor = int(input('Digite um valor:'))
op = input('Escolha um operador'
           '[1] Soma '
           '[2] Subtração'
           '[3] Multiplicação'
           '[4] Divisão')


while (aux <=10):
        if op == '1':
            print('{} + {} = {}'.format(aux, valor, (aux + valor)))
            aux = aux + 1
        elif op == '2':
            print('{} - {} = {}'.format(aux, valor,(aux - valor)))
            aux  += 1
        elif op == '3':
            print('{} * {} = {}'.format(aux, valor,(aux * valor)))
            aux += 1
        elif op == '4':
            print('{} / {} = {}'.format(valor , aux, (aux // valor)))
            aux+= 1
