km  = float(input('Qual a distancia da viagem? '))

if km <= 200:
    passagem = km * 0.50
    print('O valor da passagem é R$ {}'.format(passagem))
else:
    passagem = km * 0.45
    print('O valor da passagem é R$ {}'. format(passagem))