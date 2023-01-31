from random import randint
computs = randint(0, 10)
print('Sou seu computador.. Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computs:
        acertou = True
    else:
        if jogador < computs:
            print('Mais...tente mais uma vez.')
        else:
            print('Menos...tente mais vez.')
print('Acertou com {} tentativas. Parabens'.format(palpites))

# number = random.randint(0, 5)

# guess =int(input("Guess a number between 0 and 5: "))
# print("Loanding...")
# sleep(1)
# c = 0
# while guess != number:
#     if guess > number:
#         print("smaller, try again...")
#     else:
#         print("Bigger, try again...")

#     guess = int(input("Guess a number between 0 and 5: "))
#     if guess > 5:
#         print("This number is not between 0-5, try again!")
#     c += 1
# print(f"You got it right after {c} tries, You won!!")