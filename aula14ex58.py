# 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
tentativas = 1
computador = random.randint(0, 10)
print('\033[34m Olá. Acabei de pensar em um número entre 0 e 10. Será que você consegue acertar?\033[m')
jogador = int(input('Tente acertar o número: '))
while computador != jogador:
    if jogador < computador:
        jogador = int(input('Mais.. Tente novamente: '))
    else:
        jogador = int(input('Menos.. Tente novamente: '))
    tentativas += 1
    while 0 < jogador > 10:
        jogador = int(input('Opção inválida. Tente novamente. '))
print(f'\033[32m Parabéns! Você acertou com {tentativas} tentativas.\033[m')
