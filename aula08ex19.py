# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo o nome
# dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print(f'O aluno mais baitola é {escolhido}.')