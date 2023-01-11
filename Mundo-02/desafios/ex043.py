peso = int(input('Qual é seu peso (kg)?: '))
altura = float(input('Qual é a sua altura (m)?: '))
# (altura*altura)
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('vc está ABAIXO DO PESO normal')
elif imc <= 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')
elif imc <= 30:
    print('Voce esta em SOBREPESO')
elif imc <= 40:
    print('vc esta em OBESIDADE')
else:
    print('vc esta em OBESIDADE MORBIDA TOME CUIDADO')