palavras = ('aprender','progamar','liguagem','Python', 'Curso','Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado','Progamador')
for p in palavras:
    print(f'\n Na palavra {p.upper()} Temos ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')