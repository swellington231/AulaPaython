print('*Super progressão aritimetica.*')
print("="* 30)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=" ")
        termo = termo + razão
        cont = cont + 1
    print('PAUSE')
    mais = int(input('Quantos termos você que ver Mais? '))
print('FIM o total mostrado foi {} TERMOS'.format(total))