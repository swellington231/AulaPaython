times = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia'
         'Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
print('=' * 30)
print(f'Os cincos time primerio conolacod são:  {times[:5]}')
print('='*30)
print(f'Colocação dos ultimos 4 colocados são : {times[-4:]}')
print('=' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=' * 30)
print(f'A Chapecoense está na posição: {times.index("Chapecoense")}ª  Posição')