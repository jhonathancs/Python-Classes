print('-='*20)
print('Analisador de triangulos')
print('-='*20)

r1 = float(input('digite a reta1: '))
r2 = float(input('digite a reta2: '))
r3 = float(input('digite a reta3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima PODEM FORMAR um triangulo')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo')