# num = 0
# cont = 0
# soma = 0
num = soma = cont = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma+=num
    cont+=1
    num = int(input('Digite um numero [999 para parar]: '))

print('Vc digitou {} numeros a soma entre eles é {}'.format(cont,soma))