velocidade = float(input('Digite a velocidade atual do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você excedeu o limite de velocidade que é de 80 KM/h')
    print('Sua multa é de R$ {:.2f}'.format(multa))

else:
    print('Dirija com segurança! ')
