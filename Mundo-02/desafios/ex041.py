from datetime import date

nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificacao: MIRIM')
elif 14 >= idade:
    print('Classificacao: INFANTIL')
elif 19 >= idade:
    print('Classificacao: JUNIOR')
elif 25 >= idade:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
