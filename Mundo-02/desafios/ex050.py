soma = 0
cont = 0
for c in range(1,7):
    n = int(input('digite o {} valor aqui: '.format(c)))
    if n%2 == 0:
        soma+=n
        cont+=1
    # else:
    #     print('esse numero nao é par')
print('VOCE informou {} numeros PARES e o valor da soma é {}'.format(cont,soma))