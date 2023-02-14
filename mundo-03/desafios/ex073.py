times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')

print('=-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('=-='*20)
print(f'Os 5 primeiros são {times[:5]}')
print('=-='*20)
print(f'Os 4 primeiros são{times[-4:]}')
print('=-='*20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-='*20)
print(f'O chapecoense esta na {times.index("Chapecoense") + 1}ª posição' )
