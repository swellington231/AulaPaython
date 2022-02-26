peso = int(input('Informe peso de uma pessoa: '))
altura = float(input('Qual a altura: '))

imc = peso / (altura * altura)

if imc < 18.5 :

    print('O IMC é {:.1f} você está abaixo do peso'.format(imc))
elif imc >= 18 and imc <=25:
    print('O IMC é de {:.1f} seu peso está ideal'.format(imc))
elif imc >25 and imc <=30 :
    print('O IMC é de {:.1f} você está com SOBREPESO'.format(imc))
elif imc > 30 and imc <=40:
    print('O IMC é de {:.1f} você está obesa'.format(imc))
else:
    print('O IMC é de {:.1f} você esta com obesidade Morbida'.format(imc))