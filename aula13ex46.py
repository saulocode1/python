# 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
# até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
print(emoji.emojize(':sparkles:' * 22, use_aliases=True))
print('Contagem regressiva para no ano novo!')
print(emoji.emojize(':sparkles:' * 22, use_aliases=True))
for c in range(10, 0, -1, ):
    sleep(1)
    print(c)
sleep(1)
print(emoji.emojize(':sparkles: :fireworks: FELIZ ANO NOVO!! :sparkles: :fireworks:', use_aliases=True))
