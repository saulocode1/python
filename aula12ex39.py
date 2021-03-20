from datetime import date
ano = int(input('Qual ano você nasceu? '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano}, tem {idade} anos em {date.today().year}.')
if idade < 18:
    print(f'Você terá que se alistar em {date.today().year + (18 - idade)}. Daqui há {18 - idade} anos.')
elif idade > 18:
    print(f'Você deveria ter se alistado em {date.today().year - (idade - 18)}. Há {idade - 18} anos.')
else:
    print('Você terá que se alistar este ano.')
