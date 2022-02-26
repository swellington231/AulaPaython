class retangulo:
    def __init__(self,base,altura,):
        self.base = base
        self.altura = altura
        self.area = 0


    def muda_valor(self, novo_valor1,novo_valor2):
        self.base = novo_valor1
        self.altura = novo_valor2

    def calc_area(self):
        return self.base * self.altura

    def valor_lado(self):
        return self.base * self.altura / 2

    def calc_perimetro(self):
        return (self.base + self.altura) * 2


valor = retangulo(10, 5)
valor.muda_valor(9, 5)
print(f'O calculo da aréa do retangulo é {valor.calc_area()} cm' )
print(f'O valor dos lados é {valor.valor_lado()}')
print(f'O valor do primetro é {valor.calc_perimetro()} cm' )

print('=' * 40)
print('C)')

# c)

cp = float(input('Digite a altura: '))
ar = float(input('Digite a largura: '))
larg_piso = float(input('Digite a largura do piso: '))
comp_piso = float(input('Digite o comprimento do piso: '))
p = retangulo(cp, ar)
ap = retangulo(larg_piso, comp_piso)
area = p.calc_area()
area_piso = ap.calc_area()
rodapé =2 * (cp + ar)




print(f'A aréa é {p.calc_area()} Cm')
print(f'A quantidade de piso é {area / area_piso:.1f}')
print(f'A quantidade de rodapé é {rodapé}')


