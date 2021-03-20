# 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
    continuar = ' '
    while continuar not in 'Ss:':
        continuar = str(input('Quer continuar? [S/N] '))
print(f'Você digitou o número {tupla[num]}.')
################################################################

'''while True:
    num = int(input('Digite um número de 0 a 20: '))
    print(f'Você digitou o número {tupla[num]}.')
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn:':
        print('Tente novamente. ', end='')
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break'''


