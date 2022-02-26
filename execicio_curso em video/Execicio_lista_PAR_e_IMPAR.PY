c = [[], []]
tem = 0

for i in range(1,8):
    tem = (int(input(f'Digite o {i}º valor: ')))
    if tem % 2 == 0:
        c[0].append(tem)
    else:
        c[1].append(tem)
c[0].sort()
c[1].sort()
print(f'Os numero pares são: {c[0]}')
print(f'Os numeros Impares são{c[1]}')