from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for pess in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    pessoa = atual - nasc
    if pessoa >= 18:
        totMaior += 1
    else:
        totMenor += 1
print('São {} Pessoas Maiores de idade'.format(totMaior))
print('São {} Pessoas Menores de idade'. format(totMenor))



