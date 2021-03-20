# 016.  Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção Inteira.

import math
a = float(input('Digite um número real: '))
print('{} arredondado é {}.'.format(a, math.floor(a)))

from math import floor
b = float(input('Digite um número real: '))
num = floor(b)
print('{} arredondado é {}.'.format(b, num))

from math import trunc
c = float(input('Digite um número: '))
print('{} em sua porção inteira é {}.'.format(c, trunc(c)))




