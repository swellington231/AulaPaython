
ips = open('ips.txt', 'w+')
ips.write('200.135.80.9\n')
ips.write('192.168.1.1\n')
ips.write('8.35.67.74\n')
ips.write('257.32.4.5\n')
ips.write('85.345.1.2\n')
ips.write('1.2.3.4\n')
ips.write('9.8.234.5\n')
ips.write('192.168.0.256\n')
print(ips.read())
ips.close()
import os


def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True


if os.path.exists('ips.txt'):
    ips = open("ips.txt", "r")
    lista_ips = ips.read().split("\n")

    validos = []
    invalidos = []

    for ip in lista_ips:
        if ip_valido(ip) == True:
            validos.append(ip)

        else:
            invalidos.append(ip)

    if len(validos) > 0 or len(invalidos) > 0:
        arquivo_relatorio = open("resposta.txt", "wt")

        if len(validos) > 0:
            arquivo_relatorio.write("[Ip válidos:]\n")
            for valido in validos:
                arquivo_relatorio.write(valido + "\n")


        if len(invalidos) > 0:
            arquivo_relatorio.write("\n[Ip inválidos:]\n")
            for invalido in invalidos:
                arquivo_relatorio.write(invalido + "\n")

        arquivo_relatorio.close()
else:
    print("O ips.txt com a lista de ips não existe")
ips = open('resposta.txt', 'r')
print(ips.read())
