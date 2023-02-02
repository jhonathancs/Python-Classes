from datetime import date
atual = date.today().year
nasc = int(input('qual o ANO do seu nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))

# Outra utilidade das aspas triplas é declarar uma string que necessita de várias linhas.
print('''qual é o seu genero:
[ 1 ] MASCULINO
[ 2 ] FEMININO
''')

opcao1 = int(input('digite aqui seu genero: '))


if idade == 18 and opcao1 == 1:
    print('vc tem que se alistar imediatamente')
    print('vc tem que se alistar nesse ano de {}'.format(atual))
elif idade > 18 and opcao1 == 1:
    saldo = idade - 18
    ano = atual - saldo
    print('vc ja passou {} anos, vc ja deveria ter se alistado'.format(saldo))
    print('seu alistamento ja foi feito no ano de {}'.format(ano))
elif idade < 18 and opcao1 == 1:
    saldo = 18 - idade
    ano = atual + saldo
    print('vc ainda nao tem que se alistar, espere {} anos para se alistar'.format(saldo))
    print('seu alistamento sera no ano de {}'.format(ano))

elif opcao1 == 2:
    print('As mulheres nao precisa de alistamento')