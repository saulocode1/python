# 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulheres_men = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Qual o sexo? [M/F] ')).strip().lower()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 18:
        mulheres_men += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if continuar == 'n':
        break
print(f'Há {maiores} pessoas maiores de idade. {homens} homens foram cadastrados. {mulheres_men} mulheres menores de 18 anos.')
