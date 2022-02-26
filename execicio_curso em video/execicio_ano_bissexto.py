#from calendar import isleap
from datetime import date

ano = int(input('Digite um ano a para o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year

if  ano % 4 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano de {} BISSEXTO'.format(ano))
else:
    print('O ano não {} é BISSEXTO'.format(ano))