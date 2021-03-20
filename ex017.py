d = float(input('Qual a distância da sua viagem em km? '))
a = d * 0.50
b = d * 0.45
if d <= 200:
    print('O valor da sua passagem é R${:.2f}.'.format(a))
else:
    print('O valor da sua passagem é R${:.2f}.'.format(b))
