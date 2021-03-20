# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
 [ 1 ] converter para Binário
 [ 2 ] converter para Octal
 [ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido em binário é {bin(num)[2:]}.')
elif opção == 2:
    print(f'{num} convertido em octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida.')
