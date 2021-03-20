# 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o
# valor digitado for ímpar, desconsidere-o.
cont = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c} valor: '))
    if c % 2 == 0:
        soma += c  # somatório. 0 + n1, n1 + n2, n2 + n3...
        cont += 1  # contador. contando 1 a cada num
print(f'O somatório dos {cont} números pares é {soma}.')
