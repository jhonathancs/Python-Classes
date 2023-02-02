numero = int(input('Digite um numero inteiro: '))
# Outra utilidade das aspas triplas é declarar uma string que necessita de várias linhas.
print('''escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')

opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('nao temos essa opcao. Somente os valores acima')