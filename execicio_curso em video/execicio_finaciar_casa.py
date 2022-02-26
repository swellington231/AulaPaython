valor = float(input('Qual é o valor o imovel? '))
anos = int(input('Quantos anos de finaciamento? '))
salario = float(input('Qual o valor do seu salario? '))
anos = anos * 12
prestacao = valor / anos
print('Para uma casa de {} a prestação é {:.2f}'.format(valor, prestacao))

if prestacao <= salario * 30 / 100:
    print('PARABÉNS, eu finaciamento foi aprovado: ')


elif prestacao > salario * 30 / 100:
    print('Seu finaciamnto não foi aprovado')

