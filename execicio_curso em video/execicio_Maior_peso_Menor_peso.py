# lista = []
# for pess in range(1,5):
#     peso = float(input('Digite o {}º peso: '.format(pess)))
#     lista.append(peso)
# print('O maior peso foi {}'.format(max(lista)))
# print('O menor pes foi {} '.format(min(lista)))
menor = 0
maior = 0
for pess in range(1,6):
    peso = float(input('Digite o {}º peso:'.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            peso = menor
print('O maior peso foi {}KG.'.format(maior))
print('O menor peso foi {} KG'.format(menor))
