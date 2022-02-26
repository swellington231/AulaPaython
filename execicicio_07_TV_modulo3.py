class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume


    def mudarcanal(self, c:int):
        if c >= 1 and c <= 80:
            self.canal = c
            print(f'Bem vindo ao Canal: {r.canal}')
        else:
            print('ERRO! Canal não existe: ')

    def aumentarVolume(self, volum:int):
        if volum >= 0 and volum <= 90:
            self.volume  = volum
            print(f'Volume está em {r.volume}')
        else:
            print('ERROR! Escolha um numero entre 0 e 90:')


c = int(input('Digite o canal: '))
v = int(input('Digite o Volume: '))
r = Tv(c,v)

r.mudarcanal(c)
r.aumentarVolume(v)






