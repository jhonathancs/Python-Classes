nome = str(input('digite seu nome completo: ')).strip()
n = nome.split()


print('muito prazer em te conhecer! {}'.format(nome))
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[-1]))
# print('outra forma de fazer é {}'.format([len(n)-1]))