n = str(input('digite seu nome completo: '))

print('analisando seu nome..')
print('seu nome em maiusculas é {}'.format(n.upper()))
print('seu nome em minusculas é {}'.format(n.lower()))
print('seu nome tem ao todo {}'.format(len(n) - n.count(' ')))
print('o seu primeiro nome tem {}'.format(n.find(' ')))