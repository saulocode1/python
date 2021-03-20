# 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para saber sua tabuada: '))
print(f'A tabuada de \033[32m{n}\033[m é: ')
print('-' * 11)
for c in range(1, 11):
    print(f'{n} * {c} = {n * c}')
print('-' * 11)
