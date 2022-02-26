matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
total = 0
par = scol = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite a posição [{l}] e [{c}]: '))
total = l + c

for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end=' ')
        if matriz[l][c] % 2 ==0:
            par = par + matriz[l][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c]> maior:
            maior = matriz[1][c]

print(f'Os numeros pares são: {par}')
print(f'A soma da terceira coluna é: {scol}')
print(f'O maior numero da segunda linha é {maior}')
