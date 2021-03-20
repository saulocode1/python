maior = menor = 0
num = list()
for v in range(1, 6):
    num.append(int(input('Digite um número: ')))
    if v == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior {maior}')
print(num)
