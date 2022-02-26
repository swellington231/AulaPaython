print('Programa Progressão Aritimetica ')
print("=" *30)
primeiro = int(input("Primeiro Termo: "))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} -> '.format(termo),end=" ")
    termo +=  razão
    cont = cont + 1
print('FIM')

