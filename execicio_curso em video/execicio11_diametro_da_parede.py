larg = float(input('Largura da Parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
tinta = area / 2
print('Sua area de parde tem a dimessão de {} X {} \n se ua area é de {:.2f} m²'.format(larg, alt, area))
print('Para pintar a parde você precisa de {} litro de tinta'.format(tinta))