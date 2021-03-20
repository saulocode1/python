a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Podem formar um triângulo.')
else:
    print('Não podem formar um triângulo.')