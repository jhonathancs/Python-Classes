from datetime import date
atual = date.today().year
totMaior=0
totMenor=0
for c in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totMaior+=1
        # print(totMaior)
    else:
        totMenor+=1
print('Ao todo tivemos {} pessoas MAIOR de idade'.format(totMaior))
print('E tambem tivemos {} pessoas MENORES de idade'.format(totMenor))