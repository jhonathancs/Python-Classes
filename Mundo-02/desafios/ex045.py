from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

choice = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('COMPUTADOR jogou {}'.format(itens[computador]))
print('JOGADOR jogou {}'.format(itens[choice]))
print('-='*11)

if computador == choice:
    print('EMPATE')
elif (choice == 0 and computador == 1) or (choice == 1 and computador == 2) or (choice == 2 and computador == 0):
    print('VOCE PERDEU')
else:
    print('VC GANHOU')