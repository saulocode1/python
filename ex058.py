# 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''print('=' * 30)
print('{:^30}'.format('\033[32mBanco do Saulinho.\033[m'))
print('=' * 30)
saque = int(input('Digite o valor que quer sacar: R$ '))
cinq = saque // 50
if cinq > 0:
    print(f'Total de {cinq} cédulas de R$50.')
resto_c = saque - (cinq * 50)
vinte = resto_c // 20
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20.')
resto_v = saque - (cinq * 50) - (vinte * 20)
dez = resto_v // 10
if dez > 0:
    print(f'Total de {dez} cédulas de R$10.')
resto_d = saque - (cinq * 50) - (vinte * 20) - (dez * 10)
um = resto_d // 1
if um > 0:
    print(f'Total de {um} cédulas de R$1.')
print('=' * 30)
print('\033[34mTenha um bom dia. Volte sempre!\033[m')'''

valor = int(input('Digite o valor que quer sacar: R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} de R${céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break



