print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)


prim = int(input('Primeiro Termo: '))
raz = int(input('Razao: '))
decimo = prim + (10-1) * raz
for c in range(prim, decimo,raz):
    print('{}'.format(c), end=' -> ')
print('ACABOU!!')