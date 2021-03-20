# 018. Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
a = float(input('Digite o ângulo: '))
sin = sin(radians(a))
cos = cos(radians(a))
tg = tan(radians(a))
print('O seno desse ângulo é {:.2f}.'.format(sin))
print('O cosseno desse ângulo é {:.2f}.'.format(cos))
print('A tangente desse ângulo é {:.2f}.'.format(tg))

