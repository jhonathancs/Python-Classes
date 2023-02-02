somaidade = 0
maiorIdadeMan = 0
nomeVelho = ''
totMulher = 0
for p in range(1,5):
    print('----- {}° PESSOA -----'.format(p) )
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeMan = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeMan:
        maiorIdadeMan = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher += 1
mediaidade = somaidade/4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeMan,nomeVelho))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(totMulher))