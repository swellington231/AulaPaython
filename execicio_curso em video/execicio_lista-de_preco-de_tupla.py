listagem = ('Lapis', 2,
            'Borracha', 5,
            'Caneta', 3,
            'lapizeira', 10,
            'Caderno', 20,
            'Compasso', 4.75,
            'Garrafas', 25)
print('-' * 40)
print('LISTAGEM ESCOLAR')
print('=' * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}:', end=' ')
    else:
        print(f'R$ {listagem[pos]:5.2f}')