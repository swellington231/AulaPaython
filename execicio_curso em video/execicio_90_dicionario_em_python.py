aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Méida do {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação '] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'reprovado'

for k , v in aluno.items():
    print(f'{k} é igual a {v}')
#
# print(f'O aluno {aluno["nome"]}')
# print(f'A média foi {aluno["média"]}')
# print(f'A Situação foi {aluno["situação"]}')