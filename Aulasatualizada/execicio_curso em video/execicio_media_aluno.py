nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a seguda nota:  '))

media = (nota1 + nota2)/2

if media >= 7 :
    print('Sua média {} e você está PASSOU,  PARABÉNS '.format(media))

elif media and 5.0 or 6.9:
    print('Você está de RECUPERAÇÃO sua média foi: {} '.format(media))

elif media < 5:
    print('A sua média foi {} você foi REPROVADO'.format(media))