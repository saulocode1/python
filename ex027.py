from datetime import date
ano = int(input('Qual ano o aluno nasceu? '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: Mirim.')
elif idade <= 14:
    print('Categoria: Infantil.')
elif idade <= 19:
    print('Categoria: Junior.')
elif idade <= 25:
    print('Categoria: Sênior.')
elif idade > 25:
    print('Categoria: Master.')
