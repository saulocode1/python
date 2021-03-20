from datetime import date
a = int(input('Digite um ano. Digite 0 para ano atual: '))
if a == 0:
    a = date.today().year
if a%4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} é um ano bissexto.'.format(a))
else:
    print('{} não é um ano bissexto.'.format(a))
