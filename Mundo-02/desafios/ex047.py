from time import sleep
c = int(input('qual numero deseja ver a quantidades de pares? '))
if c%2 == 0: 
    for c in range(2,c+1, 2):
        print(c)
        sleep(0.2)
        # if c%2==0: ==> aqui ele faz mais iteracoes
else:
    print('Esse numero nao é PAR')
print('ACABOU')
    
