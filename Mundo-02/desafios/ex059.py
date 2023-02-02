import time
# from time import sleep
start_time = time.time()
end_time = start_time + 9
n1 = int(input('primeiro valor: '))
n2 = int(input('primeiro valor: '))
option = 0
while option != 5:
    print('=-=' * 5,'Escolha uma das opçoes abaixo','=-=' * 5)
    print('''    [1] Somar 
    [2] Multiplicar 
    [3] Maior
    [4] Novos numeros 
    [5] Sair do Programa''')
    print('-*-'*20)
    option = int(input('Qual é a sua opção? '))
    if option == 1:
        print('A SOMA entre {} + {} é {}'.format(n1,n2,(n1+n2)))
    elif option == 2:
        print('A MULTIPLICAÇÃO entre {} x {} é {}'.format(n1,n2,(n1*n2)))
    elif option == 3:
        print('O MAIOR numero entre {} e {} o maior é {}'.format(n1,n2,(max(n1,n2))))
    elif option == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        while time.time() < end_time:
            remaining_time = end_time - time.time()
            print("Aguarde: {:.0f} segundos para sair".format(remaining_time))
            time.sleep(1)
        print('Volte sempre...')
    else:
        print('Essa opcao nao existe')
    # sleep(2)