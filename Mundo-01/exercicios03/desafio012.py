p = float(input('qual é o preco do produto ? R$: '))

custo = p-p*0.05

print('o produto que custava R${}, na promocao com desconto de 5% vai custar R${:.2f}'.format(p,custo))