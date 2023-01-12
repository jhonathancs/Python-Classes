frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
# print(palavras)
junto = ''.join(palavras)

inverso = junto[::-1]
# print(junto)
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALINDROMO')
else:
    print('Nao é um PALINDROMO')

# inverso = ''
# for letra in range(len(junto)-1,-1,-1):
#     # print(junto[letra])
#     inverso += junto[letra]
