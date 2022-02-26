r = float(input("Quanto você tem em dinheiro? R$ "))
d = float(input('Qual o valor atual em dolar? '))
con = r / d
print('Com  {} R$ você pode comprar US$ {:.2f} centavos'.format(r,con))