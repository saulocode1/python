# 36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
meses = (anos * 12)
prestação = valor / meses
print(f'Para comprar uma casa no valor de R${valor:.2f} em {anos} anos, a prestação será de R${prestação:.2f}.')
if prestação > salário * 0.30:
    print('\033[0;31mVocê não poderá comprar a casa.\033[m')
else:
    print(f'\033[32mVocê poderá comprar a casa, em {meses} meses, e o valor da prestação será \033[1;32mR${prestação:.2f}.')
