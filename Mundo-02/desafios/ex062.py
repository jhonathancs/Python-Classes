print('Gerador de PA')
print('-=-'*10)
n = int(input('Primeiro termo: '))
razao = int(input('Primeiro termo: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont+=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ? '))
