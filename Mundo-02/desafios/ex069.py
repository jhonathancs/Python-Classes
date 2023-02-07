tot18= totMan = totWOM20 = 0
while True:
    idade=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':    
        sexo=str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    if idade >= 18:
        tot18+=1
    
    if sexo == 'M':
        totMan+=1
    
    if sexo == 'F' and idade < 20:
        totWOM20+=1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'ao total temos {totMan} HOMENS cadastrados')
print(f'ao total temos {totWOM20} MULHERES MENORES DE 20 cadastrados')