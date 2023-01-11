r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR TRIANGULO: ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCEELES!')
else:
    print('Os segmentos acima NAO PODEM FORMAR TRIANGULO')

