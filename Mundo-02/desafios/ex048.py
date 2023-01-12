# from time import sleep
# n = int(input('coloque o valor aqui: '))
s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        s += c
    # print(c)
print('A SOMA de todos os {} valor solicitados é {}'.format(cont,s))