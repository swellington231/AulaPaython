sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalido. informe seu SEXO: ')).strip().upper()[0]
print('o sexo {} foi registrado com sucesso! '.format(sexo))