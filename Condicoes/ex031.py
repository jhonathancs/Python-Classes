distancia = float(input('qual é a distancia da sua viagem? '))
print('vc esta prestes a comecar uma viagem de {} km.'.format(distancia))
precio = distancia * 0.5 if distancia<=200 else distancia*0.45

# if distancia <= 200:
#     precio = distancia * 0.50
# else:
#     precio = distancia * 0.45
print('e o preco da sua passagem sera de R$ {:.2f}'.format(precio))