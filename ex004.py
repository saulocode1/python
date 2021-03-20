# 017. Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o
# comprimento da hipotenusa.

from math import sqrt, pow

co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
h = (pow(co, 2) + pow(ca, 2))
# print('A hipotenusa vale {}.'.format(sqrt(h)))
print(f'A hipotenusa vale {sqrt(h):.2f}.')

from math import hypot

co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hi = hypot(co, ca)
print('A hipotenusa vale {:.2f}.'.format(hi))
