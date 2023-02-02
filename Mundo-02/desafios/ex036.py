casa = float(input('Valor da casa: R$ '))
salario = float(input('salario do comprador: R$ '))
anos = int(input('quantos anos de financiamento? '))

prestacao = casa/(anos * 12)
# abaixo 30% do salario sera descontado para o valor da casa
minimo = salario * 30/100

print('para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestimo concedido')
else:
    print('emprestimo negado')

print()