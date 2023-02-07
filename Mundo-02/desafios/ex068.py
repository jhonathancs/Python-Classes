from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
v=0
while True:
    n=int(input('Digite um valor: '))
    pc = randint(0,101)
    total = n+pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar ? [P / I] ')).strip().upper()[0]
    print(f'Voce jogou {n} e o computador {pc}. o total deu {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I' :
        if total % 2 == 1:
            print('Voce Venceu!')
            v+=1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente... ')

if v == 1:
    print(f'Game Over! voce venceu {v} vez.')
else:
    print(f'Game Over! voce venceu {v} vezes.')