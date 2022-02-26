dias = float(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de KM rodado: '))
# custo_dia = 60
# km_rodado = 0.15
# total = km * km_rodado + dias * custo_dia
total = (dias * 60 ) + (km * 0.15)
print(' O Km rodado foi {}\n O aluguel por {:.0f} dia(s) \n Ficou no valor de R$ {:.2f} reais '.format(km, dias, total))
