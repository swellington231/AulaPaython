preço = float(input('Qual o valor do produto? '))
novo = preço - (preço *5 / 100)
print('O valor do produto é {} e ficou R$ {:.2f} com 5% de desconto'.format(preço, novo))
