
class pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def imprimenome(self):
        print(self.nome, self.idade)
n = pessoa('Maria', '33')
n2 = pessoa('João', '55')
n.imprimenome()
class estudante(pessoa):
    pass
y = estudante('Wellington', 39)
y.imprimenome()

# class A:
#     a = 1
#     __b = 2
# class B(A):
#     __C = 3
#     def __init__(self):
#         print(self.a)
#         print(self.__c)
# a = A()
# print(a.a)
# b = B()
# print(b.__b)
# print(b.__c)

#Polimofismo

# class FormaGeometrica():
#     def calc_area(self):
#         pass
# class quadrado():
#     def __init__(self, base):
#         self.base = base
#
#     def cal_area(self):
#         return self.base *self.base
# class circulo(FormaGeometrica):
#         def __init__(self, raio):
#             self.raio = raio
#         def cal_area(self):
#             return self.raio * self.raio * 3.14
#
#
# quad1 = quadrado(4)
# quad2 = quadrado(5)
# cir1 = circulo(1)
# circ2 = circulo(2)
#
# forma_geometrica = [quad1,quad2,cir1,circ2]
# soma = 0
# for forma in forma_geometrica:
#     soma = soma + forma.cal_area()
#     print('A area doi de {}'.format(soma))