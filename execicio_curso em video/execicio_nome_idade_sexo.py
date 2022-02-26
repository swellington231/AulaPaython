mediaIdade = 0
maisVelho = 0
maioridadehome =0
totMulher = 0

for p in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).upper().strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo F/M {}ª Pessoa:  '.format(p))).upper().strip()
    mediaIdade = idade / p
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        maisVelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        maisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher = totMulher + 1
print('O home mais velho tem {} anos e o nome dele é {}'.format(maioridadehome,maisVelho))
print('O total de mulher com menos de 20 anos é {}'.format(totMulher))







