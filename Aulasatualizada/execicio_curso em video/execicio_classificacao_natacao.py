from datetime import date
nasc = int(input('Qual o ano de nascimento? '))

atual = date.today().year
idade = atual - nasc

if idade <= 9 :
    print('Este atleta tem {} anos e está na equipe MIRIM'.format(idade))

elif idade <= 14 :
    print('Este atleta tem {} anos e está na equipe INFANTIL'.format(idade))

elif idade <= 19 :
    print('Este atlta tem {} anos e está na EQUIPE JÚNIOR'.format(idade))

elif idade <= 25:
    print('Este atleta tem {} e está na equipe SÊNIO'.format(idade))

else:
    print('Este atleta tem {} anos e é MATER'.format(idade))