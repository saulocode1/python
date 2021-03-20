num = list()
continuar = ''
while True:
    a = num.append(int(input('Digite um número: ')))
    if a in num:
        num.remove(a)
        print('Numero removido')

    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()
    if continuar in 'n':
        break
print(num)