resp = 'S'
soma=quant=media=maior=menor= 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma+=num
    quant+=1
    if quant == 1:
        maior=menor=num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
media = soma/quant
print('Vode digitou {} numeros e a media foi {}'.format(quant,media))
print('O MAIOR numero é {} e o MENOR é {}'.format(maior,menor))
print('Acabou')


# c=num=soma=cont=0
# c=0
# num=0
# soma=0
# num = int(input('Digite um numero: '))
# while c != 'N':
#     num = int(input('Digite um numero: '))
#     c = str(input('Quer Continuar? [S/N]')).upper()
#     soma+=num
#     cont+=1
#     # if num 

# print('vc digitou {} numeros e a media foi {}'.format(cont,soma/cont))
# print('O maior valor foi de {} menor foi de {}'.format(maior,menor))