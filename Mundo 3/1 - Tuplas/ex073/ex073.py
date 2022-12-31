#  Ex073 - Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Corinthians.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(30 * '-=')
print(f'Lista de times do Brasileirão: {times}')
print(30 * '-=')
print(f'Os 5 primeiros são: {times[:5]}')
print(30 * '-=')
print(f'Os 4 últimos são: {times[16:]}')
print(30 * '-=')
print(f'Times em ordem alfabética: {sorted(times)}')
print(30 * '-=')
print(f'O Corinthians está na {len(times[:4])}ª posição')
