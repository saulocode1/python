a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Podem formar um triângulo ', end='')
    if a == b == c:
        print('equilátero.')
    elif a != b != c != a:
        print('escaleno.')
    else:
        print('isósceles.')
else:
    print('Não podem formar um triângulo.')
