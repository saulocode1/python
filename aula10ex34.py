s = float(input('Qual o seu salário? R$ '))
a = s * 1.10
b = s * 1.15
if s >= 1250:
    # novo = s * 1.10
    print('Seu novo salário será R${:.2f}.'.format(a))
else:
    # novo = s * 1.15
    print('Seu novo salário será R${:.2f}.'.format(b))
    # print(f'Seu novo salário será {b:.2f}')


