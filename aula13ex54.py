# 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Qual ano você nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas de idade.')
