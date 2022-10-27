import math
op = float(input('insira o cateto oposto: '))
oa = float(input('insira o cateto adjacente: '))

hp = math.hypot(op,oa)

print('o valor da hipotenusa é {:.2f}'.format(hp))