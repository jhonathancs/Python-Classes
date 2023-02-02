from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-'*20)
print('vou pensar em um numero tente advinhar')
print('-=-'*20)
player = int(input('em que numero o pc esta pensando? ')) 
print('processando...')
sleep(3)
print('parabens voce conseguiu me vencer'
if pc == player
else 'errou pensei no numero {} e vc disse {} tente outra vez'.format(pc,player))
# print('o numero aleatorio é {}'.format(pc))