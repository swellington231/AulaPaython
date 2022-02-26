num = cont = soma = 0
while True:
    num = int(input('Digite um numero (999 para parar: '))
    if num !=999:
        soma = soma + num
        cont +=1

    else:
        break

print(f'A soma dos {cont} valores foi {soma}')
print("FIM")