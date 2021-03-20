# Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome é minúsculas é {nome.lower()}')
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
