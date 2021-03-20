# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

import math
f = 1
while f != 0:
    f = int(input('Digite um número: '))
    print(f'O fatorial de {f} é {math.factorial(f)}')
