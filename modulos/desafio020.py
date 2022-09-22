import random
sa = input('primeiro aluno: ')
ta = input('primeiro aluno: ')
pa = input('primeiro aluno: ')
qa = input('primeiro aluno: ')

lista = [sa,ta,pa,qa]

random.shuffle(lista)
print('a ordem de apresentacao sera {}'.format(lista))