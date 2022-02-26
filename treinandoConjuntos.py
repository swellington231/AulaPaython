setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
a = setx | sety | setz
b = setx & sety

print(a)
print(b)
print(setx.issubset(sety),(setz))
print(setx.difference(sety))