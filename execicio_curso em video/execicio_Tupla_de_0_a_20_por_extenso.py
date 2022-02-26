extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze', 'Doze', 'Treze',
           'Quatoze', 'Quinze',  'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        break
print(f'O numero digitado foi: {extenso[num]}')