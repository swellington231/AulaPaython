frase = 'Curso em Video Python'
print(frase.count('O')) contando caractere
print(len(frase.strip())) # a função striper remove os espaço indesejados antes e depois.
print(frase.upper()) # a função upper trasforma as lestras de minuscul para maiscula.
frase = frase.replace('Python', 'Androide')# a função reolace altera a frase de uma palavra.
print(frase.lower().find('Curso'))# O comando find verifica e mostra a prosição da palavra.
print(frase.split())# A função split fatia ou divid a frase.
dividido = frase.split()
print(dividido[0][0])# o primeiro [] busca a posição da frase o segundo a posição da letra