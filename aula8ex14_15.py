 # 014. Escreva um programa que converta uma temperatura digitando em
# graus Celsius e converta para graus Fahrenheit.

c = float(input('Qual a temperatura em celsius? '))
f = float(c * 9 / 5 + 32)
k = float(c + 273.15)
print('{}ºC em Fahrenheit é {}ºF, e em Kelvin {}ºK.'.format(c, f, k))

# 015. Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.

d = float(input('Quantos dias alugados? '))
k = float(input('Quantos km rodados? '))
dia = float(d * 60)
km = float(k * 0.15)
t = dia + km
print('O total a ser pago é R${:.2f}'.format(t))
