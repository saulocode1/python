# 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice

print('''[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura''')
opção = int(input('Qual sua opção? '))
pc = choice([1, 2, 3])
if opção == pc:
    print('Empate.')
elif opção == 1 and pc == 2:
    print('Ganhei! Escolhi papel e você, pedra :D')
elif opção == 1 and pc == 3:
    print('Você ganhou. Escolhi tesoura e você, pedra :(')
elif opção == 2 and pc == 1:
    print('Você ganhou. Escolhi pedra e você, papel :(')
elif opção == 2 and pc == 3:
    print('Ganhei! Escolhi tesoura e você, papel :D')
elif opção == 3 and pc == 1:
    print('Ganhei! Escolhi pedra e você, tesoura :D')
elif opção == 3 and pc == 2:
    print('Você ganhou. Escolhi papel e você, tesoura :(')
