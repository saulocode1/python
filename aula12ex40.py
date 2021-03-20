# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1 + n2) / 2
print(f'A média do aluno é {m:.2f}.')
cores = {'limpa': '\033[m',
         'verm': '\033[31m',
         'verd': '\033[32m',
         'amar': '\033[33m'}
if m < 5:
    print(cores['verm'],'Reprovado.', cores['limpa'])
elif 5 > m < 6.9:
    print(cores['amar'], 'Recuperação.', cores['limpa'])
elif m >= 7:
    print(cores['verd'], 'Aprovado.', cores['limpa'])
