# 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
gasto = menor_mil = barato = cont = 0
nome_barato = ''
while True:
    produto = str(input('Qual produto? '))
    preço = float(input('Qual o preço? R$'))
    cont += 1
    gasto += preço
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if preço < 1000:
        menor_mil += 1
    if cont == 1 or preço < barato:
        barato = preço
        nome_barato = produto
    else:
        if preço < barato:
            barato = preço
            nome_barato = produto
    if continuar in 'n':
        break
print(f'O total gasto foi R${gasto}. {menor_mil} produtos abaixo de R$1000.00. O produto mais barato é {nome_barato} e '
      f'custa R${barato:.2f}.')

