velocidade = float(input('qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('multado! vc excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('vc deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('dirija com seguranca')