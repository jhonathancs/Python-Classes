from time import sleep
n = int(input('Digite um numero para ver sua tabuada: '))

for c in range(0,11):
    print('{} X {} = {}'.format(n, c, n*c))
    sleep(0.4)
