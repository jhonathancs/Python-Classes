print('Gerador de PA')
print('-=-'*10)
n = int(input('Primeiro termo: '))
pa = int(input('razao da PA: '))

termo = n
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += pa
    cont+=1
print('FIM')