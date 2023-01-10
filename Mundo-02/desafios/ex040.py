nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1+nota2) / 2

print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1,nota2,media))

if media > 7:
    print('o aluno esta APROVADO!!')
# elif media >= 5 and media < 7:
elif  7 > media >= 5 :
    print('o aluno esta de RECUPERACAO')
else:
    print('o aluno esta REPROVADO')