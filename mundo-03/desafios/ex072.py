cont = ('zero','um','dois','tres','quatro',
'cinco','seis','sete','oitro','nove','dez',
'onde','doze','treze','catorze','quinze',
'dezeseis','dezessete','dezoito','dezonove','vinte')

while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end='')
    print(f'Voce Digitou o numero {cont[num]}')
    print(' ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
    