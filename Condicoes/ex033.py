a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
# verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))

# if a < b and a < c:
#     print('o menor valor é {}'.format(a))

# if b < a and b < c:
#     print('o menor valor é {}'.format(a))
# if c < a and b < c:
#     print('o menor valor é {}'.format(a))