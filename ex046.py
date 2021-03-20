# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''\033[31m        [ 1 ] - Somar
        [ 2 ] - multiplicar
        [ 3 ] - maior
        [ 4 ] - novos números
        [ 5 ] - sair do programa\033[m''')
    opção = int(input('>>>> Digite a opção: '))
    if opção == 1:
        print(f'\033[34mA soma entre {n1} e {n2} é {n1 + n2}.\033[m')
    elif opção == 2:
        print(f'\033[34mA multiplicação entre {n1} e {n2} é {n1 * n2}.\033[m')
    elif opção == 3:
        if n1 > n2:
            print(f'\033[34m{n1} é maior que {n2}.\033[m')
        else:
            print(f'\033[34m{n2} é maior que {n1}.\033[m')
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 12)
    sleep(1)
print('Fim do programa.')

