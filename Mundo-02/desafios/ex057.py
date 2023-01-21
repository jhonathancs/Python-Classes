n = str(input('Informe seu sexo: [M/F]: ')).upper()
while n not in 'MmFf':
    n = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
    # if n != 'M':
    #     print(n)
print('Sexo {} registrado com sucesso'.format(n))