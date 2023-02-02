# print('\033[7;33;44mOla, mundo\033[m')
nome = 'Jhonathan'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',        
         'amarelo': '\033[33m',        
         'pretoebranco': '\033[7;30m'        
}
# print('ola! muito prazer em te conhecer, {}{}{}'.format('\033[4;35m',nome,'\033[m'))
print('ola! muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'],nome,cores['limpa']))