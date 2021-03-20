v = float(input('Qual a velocidade do carro? '))
m = (v - 80) * 7
if v > 80:
    print('Você ultrapassou o limite e foi multado em R${:.2f}.'.format(m))
print('Tenha um bom dia. Dirija com segurança!')

