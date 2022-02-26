num = [1,2,3,4]
# num [2] = 5 # Alterando o elemento na posição
# num.append(2)#adicionando um elemento no final da lista
# num.insert(0,8)#adcioando um elemento no inicio da lista
# num.sort(reverse=True)#imprimindo a lista na ordem reversa
# # num.pop()#retirando um elemento na lista
# # num.remove(2)#remove o elemento 2 da lista porem se o numero estiver em duas posição remove somente a primeira
# print(f'{num}Essa lista tem {len(num)} elementos')
num.sort(reverse=True)
print(num)
#
# valores = []
# for n in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# # valores.append(2)
# # valores.append(4)
# # valores.append(9)
# for c,v in enumerate(valores):#este laço esta verificando a posição e o elemento encontrado
#     print(f'para cada {c} encontrei {v} ')
#
# # lista = []
# # a = [1,2,3,]
# # # b = a # Desta forma altera as duas listaiguais pois não é uma copia
# # b = a [:]
# # b[2] = 6
#
# print(f'Lista de A: {a}')
# print(f'Lista de B:{b}')