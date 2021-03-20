# 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] - à vista no dinheiro/cheque
[ 2 ] - à vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão''')
pag = int(input('Qual a opção? '))
if pag == 1:
    total = valor - (valor * 0.10)
    print(f'O preço será R${total:.2f}.')
elif pag == 2:
    total = valor - (valor * 0.05)
    print(f'O preço será R${total:.2f}.')
elif pag == 3:
    parcela = valor / 2
    print(f'O pagamento será  em 2x de R${parcela:.2f}. O preço total será R${valor:.2f}')
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = valor * 1.20
    parcela = total / parcelas
    print(f'O pagamento será em {parcelas} parcelas de R$ {parcela:.2f} com juros. O preço total será R${total:.2f}.')
else:
    print('\033[31mOpção inválida\033[m')
