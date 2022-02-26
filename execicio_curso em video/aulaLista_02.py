# galera = [['João' , 20], ['Pedro' , 30], ['Maria ', 25] ]
# print(galera[0][0])# A primeira posição pega toda a lista João o segundo pega somente o nome João.
# print(galera[2][1])
# for p in galera: #Esse for imprime toda a lista
    #print(p[0])# pegar somente o nome da lista
    #print(p[1])#pega somente a idade de cada lista
    # print(f' {p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:]) #aqui cria uma copia da lista
    dado.clear()
for p in galera:
    if p [1] >= 21:
        print(f'{p[0]}  é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]}  é menor de idade')
        totmen += 1

print(f'Temos {totmai} maior de idade e {totmen} menor de idade')