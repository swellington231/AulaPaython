nome =str(input('Digite um nome: ')).upper()

print('O nome tem {} letras A: '.format(nome.upper().count('A')))
print('Ela aparece a primeira vez na posição: {}'.format(nome.find('A')+ 1))
print('Ela aparece na umtima posição: {}'.format(nome.rfind('A')+1))