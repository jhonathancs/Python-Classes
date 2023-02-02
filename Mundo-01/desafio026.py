frase = str(input('digite uma frase: ')).lower().strip()
print('a letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('a primeira letra A apareceu na posicao {}'.format(frase.find('a')+1))
print('a ultima letra A apareceu na posicao {}'.format(frase.rfind('a')+1))
