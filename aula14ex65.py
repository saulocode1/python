# 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

resp = 'S'
soma = quant = média = maior = menor =0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] '))
média = soma / quant
print(f'Você digitou {quant} números e a média entre eles foi {média}. O maior número foi {maior} e o menor {menor}.')