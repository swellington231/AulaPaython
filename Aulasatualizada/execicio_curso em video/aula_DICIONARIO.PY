pessoas = {'nome': 'Wellington', 'sexo': 'M', 'Idade': '39'}
# del pessoas['sexo']#Apagando um item
# pessoas['nome']= 'Naldo'# Alterando o nome do dicionario
# pessoas['peso']= 9.5# adicionado um elemento
# print(pessoas['nome'])# Imprimir o nome do dircionario
print(f'o {pessoas["nome"]} tem {pessoas["Idade"] } anos')# Para colocar em string formatada é preciso comolacr em aspas dupla
# # uma vem que a estrutura está representada com aspas simple.
# print(pessoas.keys())#Mostra somente as chaves
# print(pessoas.values())#Mostra somente os valores
# print(pessoas.items())#Mostra uma tupla com todos os valores
# for k in pessoas:# Mosta os valores das chaves
#     print(f'{k} ')
#
# for k,v in pessoas.items():#IMprime as chaves e os valores
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append([estado1,estado2])
# brasil.append(estado2)
# print(brasil[0])

#Usando for
#
# estado = dict()
# brasil = list()
#
# for n in range(0,3):
#      estado['uf'] = str(input('Unidade Federativa: '))
#      estado['sigla']= str(input('Digite a Sigla : '))
#      brasil.append(estado.copy())# faz uma copia do dicionario
#
# for c in brasil:# imprimindo a lista ESTADO
#     for k, v in c.items():
#         print(f'o campo {k} tem valor {v}')#MOSTRANDO O DIRCIONARIO

# print(c.copy())
