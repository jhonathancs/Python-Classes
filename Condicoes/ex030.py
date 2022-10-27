numero = int(input('Me diga um numero qualquer: '))
resultado = numero%2
if resultado == 0:
    print('o numero {} é Par'.format(numero))
else:
    print('o numero {} é Impar'.format(numero))