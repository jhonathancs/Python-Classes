print('{:=^40}'.format(' LOJAS JHONCS '))
compra = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao
''')

option = int(input('Qual é a opcao? '))

if option == 1:
    desconto = compra - (compra * 0.10)
elif option == 2:
    desconto = compra - (compra * 0.05)
elif option == 3:
    desconto = compra
    parcela = desconto / 2 
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif option == 4:
    desconto = compra + (compra*0.2)
    totalparc = int(input('quantas parcelas? '))
    parcela = desconto / totalparc
    print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    desconto = compra
    print('OPCAO INVALIDA de pagamento. tente novamente!')

print('Sua compra de R$ {} vai custar R$ {:.2f} no final'.format(compra,desconto))