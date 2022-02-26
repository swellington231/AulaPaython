salario = float(input('Qual é o salario do funcionario? '))
novo_salario = salario + (salario *15 / 100)
print('O salario atual é R$ {} com aumento de 15% ficou R$ {:.2f} '.format(salario, novo_salario))