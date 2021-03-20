# 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de
# idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_id = 0
velho = 0
mulher = 0
nome_velho = ''
for c in range(1, 5):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).upper()
    soma_id = soma_id + idade
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if sexo == 'M':  # 'if p == 1 and sexo in 'Mm':' tanto M quanto m funcionam.
        if c == 1:
            velho = idade
            nome_velho = nome
        else:
            if idade > velho:
                velho = idade
                nome_velho = nome
média = soma_id / 4
print(f'O homem mais velho é {nome_velho} e tem {velho} anos.')
print(f'A idade média do grupo é {média:.0f}.')
print(f'Há {mulher} mulheres menores de 20 anos.')
