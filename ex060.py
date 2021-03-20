# 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#   a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Inter', 'AtléticoMG', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'AtléticoPR', 'Bragantino',
         'Ceará', 'Corinthians', 'AtléticoGO', 'Bahia', 'Sport',
         'Fortaleza', 'Vasco', 'Coritiba', 'Botafogo', 'Chapecoense')

print(f'Lista de times: {times}')
print(f'Os 5 primeiros são {times[0:5]}.')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Os times em ordem são:', sorted(times))
print(f'Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
