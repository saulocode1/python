# 75: Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = ((int(input('Digite um valor: '))),
           (int(input('Digite outro valor: '))),
           (int(input('Digite mais um valor: '))),
           (int(input('Digite o último valor: '))))

print(f'Você digitou {numeros}.')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi mostrado na posição {numeros.index(3)}')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
