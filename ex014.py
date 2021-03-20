from random import randint
from time import sleep
computador = randint(0,5)
print('Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('Analisando...')
print('Pensei no número {}.'.format(computador))
if jogador == computador:
    print('Parabéns! Você acertou.')
else:
    print('Não foi dessa vez.')
