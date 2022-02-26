letras =list ()
listaNum = []
seq = [3,'C',5,'F','9','G',7, 'I',2,'X']
num = [0,1,2,3,4,5,6,7,8,9,]
letra =['CFGIX']


for i in seq:
    if i in num :
        listaNum.append(i)
    elif i in 'CFGIX':
        letras.append(i)
listaNum.sort(reverse=True)
tot = letras + listaNum
print(tot)
