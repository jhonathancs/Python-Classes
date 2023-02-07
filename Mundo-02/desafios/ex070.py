print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
totCompra=prod1000=menorPreco=cont=0
barato = ''
while True:
    produto=str(input('Nome do Produto: '))
    preco=int(input('Preço: R$ '))
    cont+=1

    totCompra+=preco
    
    if preco > 1000:
        prod1000+=1
    
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto
    # else:
    #     if preco < menorPreco:
    #         menorPreco = preco
    #         barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]?: ')).strip().upper()[0]
    if resp == 'N':
        break 
# print('-'*10,'FIM DO PROGRAMA','-'*10)
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {totCompra:.2f}')
print(f'Temos {prod1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto} que custa R$ {menorPreco:.2f}')