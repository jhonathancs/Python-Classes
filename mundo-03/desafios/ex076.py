listagem = (
    'lapís',1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Compasso', 9.99,
    'Mochila', 85.75,
    'Canetas', 7.50,
    'Livros', 34.90
)

print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*30)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R$ {listagem[item]:>5.2f}')
print('-'*40)