snack = ('hamburger','suco','pizza','pudim')
# print(snack)
# print(snack[1]) # segundo elemento da tupla
# print(snack[1:3]) # vai do (suco,pizza)
# print(snack[-2:]) # roda ao contrario do ultimo elemento para o primeiro (pizza,pudim)
# print(snack[:-1]) # roda ao contrario do ultimo elemento para o primeiro (ele retira o ultimo elemento)

# for c in snack: 
#     print(f'Eu vou comer {c}')
# for c in range(0,len(snack)): 
#     print(f'Eu vou comer {snack[c]}')
# print('over')    
for pos,comida in enumerate(snack): 
    print(f'Eu vou comer {comida} na posicao {pos}')
print('over')    




