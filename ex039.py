# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # separar palavras
junto = ''.join(palavras)  # juntar tudo retirando espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):  # ultima letra - 1; até a letra antes da primeira; voltando de 1 em 1
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')
