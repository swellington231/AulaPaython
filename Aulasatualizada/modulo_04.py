# while True:
#     try:
#         x = int(input("Digite um numero: "))
#         break
#     except ValueError:
#         print('ERRO! digite um numero valido')
# arqivo = open('teste.txt', 'W+')
# arqivo.close()

arquivo = open('teste.txt','w+')
arquivo.write('Teste 01\n')
arquivo.write('Teste 02 \n')
arquivo.write('Teste 04 \n')
arquivo.seek(0, 0)
print(arquivo.read())
arquivo.close()

