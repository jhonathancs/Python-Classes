maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {}° Pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR peso lido foi de {}kg'.format(maior))
print('O MENOR peso lido foi de {}kg'.format(menor))
