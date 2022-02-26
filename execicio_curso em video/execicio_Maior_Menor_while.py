opção = 'S'
numero = soma = media = maior = menor = cont = 0
while opção == 'S':
    numero = int(input('Digite um numero: '))
    opção = str(input('Quer continuar S/N: ')).strip().upper()
    soma = soma + numero
    cont = cont + 1
    if cont == 1 :
        maior = numero
        menor = numero
    else :
        if numero > maior :
            maior = numero
        if numero < menor :
            menor = numero
media = soma / cont
print('A soma de todos os numeros é {} e a média é {}'.format(cont, media))
print('O maior numero é {} e o menor numero é {}'.format(maior, menor))

print('FIM')