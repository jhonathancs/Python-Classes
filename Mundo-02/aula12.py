nome = str(input('qual é o seu nome? '))
if nome == 'jhon':
    print('q bonito nome')
elif nome=='pedro' or nome=='maria' or nome=='joao':
    print('seu nome é popular')
elif nome in 'jhon costa souza':
    print('seu nome é conhecido')
else:
    print('seu nome é bem normal')
print('tenha um bom dia, {}'.format(nome))