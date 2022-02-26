from datetime import date
ano  = int(input('Qual o ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade == 18:
    print('Você já tem {} precisa se alistar IMEDIATAMENTE '.format(idade))
elif idade > 18:
    saldo = idade - 18
    print('Você está com {} anos  e já passou {} anos de  ALISTAR.'.format(idade, saldo ))
    ano = atual - saldo
    print('Voce já passou {} do alistamento e deveria ter se alistado {}'.format(saldo, ano))

elif idade < 18:
    saldo = 18 - idade
    print('Você está com {} e ainda falta se ALISTAR {}'.format(idade, saldo))