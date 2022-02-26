cont = 0
numero = 0
soma = 0
while numero != 999 :
    numero = int(input('Digite um numero. [999] Digite para parar. '))
    if numero != 999:
        soma = soma + numero
        cont = cont+1

print(' O total de numero foi {} e a soma é {}'.format(cont, soma))
print('FIM')