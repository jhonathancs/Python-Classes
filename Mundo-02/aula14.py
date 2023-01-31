n = 1
s = 0
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n!= 0:
        if n % 2 == 0:
            par+=1
        else:
            impar+=1
print('vc digitou {} numeros pares e {} numeros impares!.'.format(par,impar))
#     # print(n)
#     # s += n

# print(s)
# print('FIm')


# from time import sleep
# c = 1
# while c < 10:
#     print(c)
#     c+=1
#     sleep(1.5)
#     # c = c + 1
# print('Fim')