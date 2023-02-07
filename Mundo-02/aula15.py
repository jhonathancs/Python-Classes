n = soma = 0
# n = int(input('Digite o seu numero aqui: '))
while True:
    n = int(input('Digite o seu numero aqui: '))
    if n == 999:
        break
    soma += n
# print(f'A Soma vale {soma}')
print('A Soma vale', soma)
# from time import sleep
# cont = 1
# # while cont <= 10:
# while True:
#     print(cont, ' ')
#     cont += 1
#     sleep(1)
# print('Acabou')