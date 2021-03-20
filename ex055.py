# 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    total = (jogador + computador)
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]  # [0] pegar só a primeira letra
    print(f'Você jogou {jogador} e computador {computador}. Total igual a {total}.')
    print(f'Deu par.' if total % 2 == 0 else 'Deu ímpar.')
    if escolha == 'p':
        if total % 2 == 0:
            print('Você ganhou.')
            cont += 1
        else:
            print('Você perdeu.')
            break
    elif escolha == 'i':
        if total % 2 == 1:
            print('Você ganhou.')
            cont += 1
        else:
            print('Você perdeu.')
            break
print(f'Você ganhou {cont} vezes.')
