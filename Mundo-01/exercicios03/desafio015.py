n = int(input('quantos dias alugados? '))
km = int(input('quantos km rodados? '))
c = 60*n
rodado = km*0.15
total = c + rodado

print('o total a pagar é de {}'.format(total))