from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'os valores sorteados foram: ',end='')

for num in n:
    print(f'{num}',end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

# while True:
#     for num in n:
#         print(f'{num}',end='')
#     print(f'\nO maior valor sorteado foi {max(n)}')
#     resp = str(input('Deseja ver novos numeros ?')).upper().split()[0]
#     if resp == 'Ss':
#         break

