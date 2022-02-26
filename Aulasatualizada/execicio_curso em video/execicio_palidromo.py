frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntos = ''.join(palavra)
inverso = juntos[::-1]
if inverso == juntos:
    print('O nome {}  o iverso  {} é PALIMDROMO'.format(juntos, inverso))
else:
    print('O nome {} não é um palidromo {} '.format(juntos, inverso))