setx = set(["apple","mango"])
sety = set(["mango", "orango"])
setz = set(["mango"])
a = setx | sety | setz
b = sety & setx

print( 'OS elemento que pertece ao conjunto são:',a)
print('O Elemento comum entre os conjuntos sety e setx é: ', b)
print(setx.issubset(sety),(setz))
print('O elemento que esta em setX e não está em sety é', setx.difference(sety))