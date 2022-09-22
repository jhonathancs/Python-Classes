import random
sa = input('primeiro aluno: ')
ta = input('primeiro aluno: ')
pa = input('primeiro aluno: ')
qa = input('primeiro aluno: ')
lista = [pa,sa,ta,qa]
s = random.choice(lista)

print('o aluno eslhido foi {}'.format(s))