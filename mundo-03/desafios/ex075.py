num = (
    int(input('Digite um numero:')),
    int(input('Digite outro numero:')),
    int(input('Digite mais numero:')),
    int(input('Digite o ultimo numero:')),
)

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posiçao')
else:
    print('O valor 3 nao foi digitado em nenhuma posiçao')
print(f'Os valores pares são: ',end=' ')
for n in num:
    if n%2 == 0:
        print(n,end=' ')
print('')